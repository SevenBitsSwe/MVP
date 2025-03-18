import unittest
from unittest.mock import Mock, patch
import uuid
from Core.ClickhouseActivityRepository import ClickhouseActivityRepository
from Core.DatabaseConnection import DatabaseConnection
from Core.ActivityDTO import ActivityDTO

class TestClickhouseActivityRepository(unittest.TestCase):
    def setUp(self):
        # Create a mock for DatabaseConnection
        self.mock_db_connection = Mock(spec=DatabaseConnection)
        # Mock for the connection result
        self.mock_connection = Mock()
        self.mock_db_connection.connect.return_value = self.mock_connection
        # Initialize the repository with the mock
        self.repository = ClickhouseActivityRepository(self.mock_db_connection)

    def test_get_activities_in_range(self):
        # Prepare test data
        test_lon = 11.8444214
        test_lat = 45.3785957
        test_max_distance = 1000
        
        # Mock data to simulate found activities
        mock_activities = [
            ["Bar Roma", "Via Roma 1", "Bar", "Bar in the center", 500.5],
            ["Ristorante Verona", "Via Verona 2", "Restaurant", "Italian restaurant", 800.2]
        ]
        
        # Configure the mock to return the data
        mock_result = Mock()
        mock_result.result_rows = mock_activities
        self.mock_connection.query.return_value = mock_result
        
        # Execute the method to test
        result = self.repository.get_activities_in_range(test_lon, test_lat, test_max_distance)
        
        # Verify the results
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][0], "Bar Roma")
        self.assertEqual(result[1][0], "Ristorante Verona")
        
        # Verify that the query is executed with correct parameters
        self.mock_connection.query.assert_called_once()
        call_args = self.mock_connection.query.call_args
        self.assertIn("parameters", call_args[1])
        params = call_args[1]["parameters"]
        self.assertEqual(params["lon"], test_lon)
        self.assertEqual(params["lat"], test_lat)
        self.assertEqual(params["max_distance"], test_max_distance)

    def test_get_activity_spec_from_name_found(self):
        # Prepare test data
        test_activity_name = "Gasperi, Almagi e Lollobrigida SPA"
        test_activity_id = uuid.uuid4()
        
        # Create a mock for the query result
        mock_result = Mock()
        mock_result.result_set = [{}]  # Necessary for length check
        mock_result.first_item = {
            'activity_uuid': str(test_activity_id),  # The name in the DB might be 'activity_uuid'
            'name': test_activity_name,
            'longitude': '11.8444214',
            'latitude': '45.3785957',
            'address': 'Contrada Altera, Montegallo, Bellamonte, Grosseto, 51021, Italia',
            'type': 'Education',
            'description': 'Training center'
        }
        
        self.mock_connection.query.return_value = mock_result
        
        # Execute the method to test
        result = self.repository.get_activity_spec_from_name(test_activity_name)
        
        # Verify the results using correct attributes of ActivityDTO
        self.assertEqual(result.activity_id, str(test_activity_id))
        self.assertEqual(result.activity_name, test_activity_name)  # Changed from name to activity_name
        self.assertEqual(result.activity_lon, 11.8444214)  # Changed from longitude to activity_lon
        self.assertEqual(result.activity_lat, 45.3785957)  # Changed from latitude to activity_lat
        self.assertEqual(result.activity_addr, 'Contrada Altera, Montegallo, Bellamonte, Grosseto, 51021, Italia')  # Changed from address to activity_addr
        self.assertEqual(result.activity_type, 'Education')  # Changed from type to activity_type
        self.assertEqual(result.activity_description, 'Training center')  # Changed from description to activity_description
        
        # Verify that the query is executed with correct parameters
        self.mock_connection.query.assert_called_once()
        call_args = self.mock_connection.query.call_args
        self.assertIn("parameters", call_args[1])
        self.assertEqual(call_args[1]["parameters"]["nome"], test_activity_name)

    def test_get_activity_spec_from_name_not_found(self):
        # Prepare mock to simulate no activity found
        test_activity_name = "Attività Inesistente"
        mock_result = Mock()
        mock_result.result_set = []  # No results found
        
        self.mock_connection.query.return_value = mock_result
        
        # Execute method to test
        result = self.repository.get_activity_spec_from_name(test_activity_name)
        
        # Verify that an empty ActivityDTO is returned using correct attributes
        self.assertIsInstance(result, ActivityDTO)
        self.assertEqual(result.activity_name,"")  # Keeps activity_name
        
        # Verify that the query was executed with correct parameters
        self.mock_connection.query.assert_called_once()
        call_args = self.mock_connection.query.call_args
        self.assertEqual(call_args[1]["parameters"]["nome"], test_activity_name)