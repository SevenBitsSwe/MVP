import unittest
from unittest.mock import MagicMock, patch
from pyflink.common.types import Row
from datetime import datetime

#TU17
# Import corretti
from Core.PositionToMessageProcessor import PositionToMessageProcessor
from Core.LLMService import LLMService
from Core.IUserRepository import IUserRepository
from Core.IActivityRepository import IActivityRepository
from Core.IFlinkSerializable import IFlinkSerializable
from Core.ActivityDTO import ActivityDTO
from Core.MessageDTO import MessageDTO
from Core.UserDTO import UserDTO
from Core.StructuredResponseMessage import StructuredResponseMessage
from Core.CustomPrompt import CustomPrompt

class TestPositionToMessageProcessor(unittest.TestCase):
    def setUp(self):
        # Mock all the outbound ports -> specify the class type
        self.ai_service = MagicMock(spec=LLMService)
        self.user_repository = MagicMock(spec=IUserRepository)
        self.activity_repository = MagicMock(spec=IActivityRepository)
        self.message_serializer = MagicMock(spec=IFlinkSerializable)
        
        # Create the istance to use in the tests
        self.processor = PositionToMessageProcessor(
            self.ai_service,
            self.user_repository,
            self.activity_repository,
            self.message_serializer
        )
        
        # Mock custmom promp which is called in open method
        self.processor.prompt_creator = MagicMock(spec=CustomPrompt)
    
    def test_open(self):
        """Test the open method which initializes the AI service and the prompt creator"""
        runtime_context = MagicMock()
        
        # Esegui il metodo da testare
        self.processor.open(runtime_context)
        
        # Verifica che i metodi necessari siano chiamati
        self.ai_service.set_up_chat.assert_called_once()
        self.assertIsNotNone(self.processor.prompt_creator)

    def test_map_no_activities(self):
        """Case test where there are no activities in the range (very rare)"""
        # Prepara i dati di input
        sensor_id = "00000000-0000-0000-0000-000000000000"
        latitude = 45.4642
        longitude = 9.1900
        timestamp = "2025-03-17 14:45:30"
        input_value = [sensor_id, latitude, longitude, timestamp]
        
        # Mock user repository and activity repository
        mock_user = MagicMock(spec=UserDTO)
        mock_user.user_uuid = "10000000-0000-0000-0000-000000000000"
        self.user_repository.get_user_who_owns_sensor.return_value = mock_user
        self.activity_repository.get_activities_in_range.return_value = []
        
        # Execute the method
        result = self.processor.map(input_value)
        
        # Verify right calls
        self.user_repository.get_user_who_owns_sensor.assert_called_once_with(sensor_id)
        self.activity_repository.get_activities_in_range.assert_called_once_with(longitude, latitude, 300)
        
        # Verify result row is composed of right values
        self.assertIsInstance(result, Row)
        self.assertEqual(result[0], "10000000-0000-0000-0000-000000000000")  # user_uuid
        self.assertEqual(result[3], "skip-this-message")  # messaggio
        self.assertEqual(result[4], 0.0)  # activity_lat
        self.assertEqual(result[5], 0.0)  # activity_lon
        self.assertEqual(result[7], latitude)  # user_lat
        self.assertEqual(result[8], longitude)  # user_lon

    def test_map_with_activities(self):
        """Case test where some activities are in the range"""
        # Mock input data
        sensor_id = "00000000-0000-0000-0000-000000000000"
        latitude = 45.4642
        longitude = 9.1900
        timestamp = "2025-03-17 14:45:30"
        input_value = [sensor_id, latitude, longitude, timestamp]
        
        # Mock userdto istance 
        mock_user = MagicMock(spec=UserDTO)
        mock_user.user_uuid = "10000000-0000-0000-0000-000000000000"
        self.user_repository.get_user_who_owns_sensor.return_value = mock_user
        
        mock_activities = [MagicMock(spec=ActivityDTO), MagicMock(spec=ActivityDTO)]
        self.activity_repository.get_activities_in_range.return_value = mock_activities
        
        mock_structured_response = MagicMock(spec=StructuredResponseMessage)
        mock_structured_response.model_dump.return_value = {
            'attivita': 'Palestra XYZ',
            'pubblicita': 'Vieni ad allenarti da noi!'
        }
        self.ai_service.get_llm_structured_response.return_value = mock_structured_response
        
        mock_activity_info = MagicMock(spec=ActivityDTO)
        mock_activity_info.activity_id = "act123"
        mock_activity_info.activity_lat = 45.4700
        mock_activity_info.activity_lon = 9.1950
        self.activity_repository.get_activity_spec_from_name.return_value = mock_activity_info
        
        mock_result_row = Row("10000000-0000-0000-0000-000000000000", "act123", "msg123", "Vieni ad allenarti da noi!", 
                             45.4700, 9.1950, "2025-03-17 14:45:30", latitude, longitude)
        self.message_serializer.create_row_from_message.return_value = mock_result_row
        
        # Esegui il metodo da testare
        result = self.processor.map(input_value)
        
        # Verifica chiamate
        self.user_repository.get_user_who_owns_sensor.assert_called_once_with(sensor_id)
        self.activity_repository.get_activities_in_range.assert_called_once_with(longitude, latitude, 300)
        self.processor.prompt_creator.get_prompt.assert_called_once_with(mock_user, mock_activities)
        self.ai_service.get_llm_structured_response.assert_called_once()
        self.activity_repository.get_activity_spec_from_name.assert_called_once_with('Palestra XYZ')
        self.message_serializer.create_row_from_message.assert_called_once()
        
        # Verifica che il risultato sia quello atteso
        self.assertEqual(result, mock_result_row)