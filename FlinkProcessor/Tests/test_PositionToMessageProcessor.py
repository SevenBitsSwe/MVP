import unittest
from unittest.mock import MagicMock
from pyflink.common.types import Row

# Import corretti
from Core.PositionToMessageProcessor import PositionToMessageProcessor
from Core.LLMService import LLMService
from Core.IUserRepository import IUserRepository
from Core.IActivityRepository import IActivityRepository
from Core.IFlinkSerializable import IFlinkSerializable
from Core.ActivityDTO import ActivityDTO
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


    def test_map_no_matching_activities(self):
        """Test case di quando le attività esistono ma non c'è un match con gli interessi dell'utente"""
        # Input data
        sensor_id = "00000000-0000-0000-0000-000000000000"
        latitude = 45.4642
        longitude = 9.1900
        timestamp = "2025-03-17 14:45:30"
        input_value = [sensor_id, latitude, longitude, timestamp]

        # Mock user
        mock_user = MagicMock(spec=UserDTO)
        mock_user.user_uuid = "10000000-0000-0000-0000-000000000000"
        mock_user.interests = ["Sport"]
        self.user_repository.get_user_who_owns_sensor.return_value = mock_user
        
        mock_activities = [
            ["Museo", "Indirizzo 1", "Cultura", "Descrizione", 100.0],
            ["Concerto", "Indirizzo 2", "Musica", "Descrizione", 200.0]
        ]
        self.activity_repository.get_activities_in_range.return_value = mock_activities
        self.activity_repository.get_activity_for_user.return_value = None

        result = self.processor.map(input_value)

        # Verifica le chiamate
        self.user_repository.get_user_who_owns_sensor.assert_called_once_with(sensor_id)
        self.activity_repository.get_activities_in_range.assert_called_once_with(longitude, latitude, 300)
        self.activity_repository.get_activity_for_user.assert_called_once_with(mock_user.interests, mock_activities)

        # Verifica il risultato
        self.assertIsInstance(result, Row)
        self.assertEqual(result[0], mock_user.user_uuid)
        self.assertEqual(result[3], "skip-this-message")


    def test_map_successful_message_generation(self):
        """Test successful message generation flow"""
        # Input data
        sensor_id = "00000000-0000-0000-0000-000000000000"
        latitude = 45.4642
        longitude = 9.1900
        timestamp = "2025-03-17 14:45:30"
        input_value = [sensor_id, latitude, longitude, timestamp]

        # Mock utente
        mock_user = MagicMock(spec=UserDTO)
        mock_user.user_uuid = "10000000-0000-0000-0000-000000000000"
        mock_user.interests = ["Sport"]
        self.user_repository.get_user_who_owns_sensor.return_value = mock_user
        
        # Mock le attività
        mock_activities = [
            ["Palestra", "Indirizzo 1", "Sport", "Centro Fitness", 100.0],
            ["Piscina", "Indirizzo 2", "Sport", "Piscina", 200.0]
        ]
        chosen_activity = mock_activities[0]
        self.activity_repository.get_activities_in_range.return_value = mock_activities
        self.activity_repository.get_activity_for_user.return_value = chosen_activity

        # Mock activity details
        mock_activity_info = MagicMock(spec=ActivityDTO)
        mock_activity_info.activity_id = "Palestra123"
        mock_activity_info.activity_lat = 45.4700
        mock_activity_info.activity_lon = 9.1950
        self.activity_repository.get_activity_spec_from_name.return_value = mock_activity_info

        # Mock la risposta AI
        mock_ai_response = MagicMock()
        mock_ai_response.model_dump.return_value = {
            'pubblicita': 'Unisciti alla nostra palestra oggi! Offerta speciale!'
        }
        self.ai_service.get_llm_structured_response.return_value = mock_ai_response

        # Mock serialized row
        expected_row = Row(
            mock_user.user_uuid,
            "Palestra123",
            str(MagicMock()),
            'Unisciti alla nostra palestra oggi! Offerta speciale!',
            45.4700,
            9.1950,
            MagicMock(),
            latitude,
            longitude
        )
        self.message_serializer.create_row_from_message.return_value = expected_row

        result = self.processor.map(input_value)

        # Verifica le chiamate
        self.processor.prompt_creator.get_prompt.assert_called_once_with(mock_user, chosen_activity)
        self.ai_service.get_llm_structured_response.assert_called_once()
        self.activity_repository.get_activity_spec_from_name.assert_called_once_with("Palestra")
        self.message_serializer.create_row_from_message.assert_called_once()

        # Verifcia il risultato
        self.assertEqual(result, expected_row)
