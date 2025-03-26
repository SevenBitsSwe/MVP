import unittest
from unittest.mock import Mock, patch
import uuid
from Core.ClickhouseUserRepository import ClickhouseUserRepository
from Core.DatabaseConnection import DatabaseConnection
from Core.UserDTO import UserDTO

#TU3
class TestClickhouseUserRepository(unittest.TestCase):
    def setUp(self):
        # Create a mock for DatabaseConnection
        self.mock_db_connection = Mock(spec=DatabaseConnection)
        # Mock for the connection result
        self.mock_connection = Mock()
        self.mock_db_connection.connect.return_value = self.mock_connection
        # Initialize the repository with the mock
        self.repository = ClickhouseUserRepository(self.mock_db_connection)

    def test_mark_user_as_occupied(self):
        # Prepare test data
        user_uuid = uuid.uuid4()
        sensor_uuid = uuid.uuid4()
        
        # Execute the method to test
        self.repository.mark_user_as_occupied(user_uuid, sensor_uuid)
        
        # Verify that the calls were executed correctly
        expected_query = f"ALTER TABLE nearyou.user UPDATE assigned_sensor_uuid = '{sensor_uuid}' WHERE user_uuid = '{user_uuid}'"
        self.mock_db_connection.connect.assert_called_once()
        self.mock_connection.query.assert_called_once_with(expected_query)
        self.mock_db_connection.disconnect.assert_called_once()

    def test_get_free_user_found(self):
        # Prepare mock to simulate a found user
        test_user_uuid = uuid.uuid4()
        mock_result = Mock()
        mock_result.result_rows = [(
            test_user_uuid,  # user_uuid
            None,  # assigned_sensor_uuid
            "Mario",  # name
            "Rossi",  # surname
            "mario.rossi@example.com",  # email
            "M",  # gender
            "1990-01-01",  # birthdate
            "single"  # civil_status
        )]
        self.mock_connection.query.return_value = mock_result
        
        # Execute the method to test
        result = self.repository.get_free_user()
        
        # Verify the results
        self.assertIsNotNone(result)
        self.assertEqual(result.user_uuid, test_user_uuid)
        self.assertEqual(result.name, "Mario")
        self.assertEqual(result.surname, "Rossi")
        self.assertEqual(result.email, "mario.rossi@example.com")
        expected_query = "SELECT user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status FROM nearyou.user WHERE assigned_sensor_uuid IS NULL"
        self.mock_connection.query.assert_called_once_with(expected_query)

    def test_get_free_user_not_found(self):
        # Prepare mock to simulate no user found
        mock_result = Mock()
        mock_result.result_rows = []
        self.mock_connection.query.return_value = mock_result
        
        # Execute the method to test
        result = self.repository.get_free_user()
        
        # Verify the results
        self.assertIsNone(result)

    def test_get_user_who_owns_sensor_found(self):
        # Prepare mock to simulate a user found with the sensor
        test_user_uuid = uuid.uuid4()
        test_sensor_uuid = uuid.uuid4()
        interests = ["sport", "music", "books"]
        
        mock_result = Mock()
        mock_result.result_rows = [(
            test_user_uuid,  # user_uuid
            test_sensor_uuid,  # assigned_sensor_uuid
            "Mario",  # name
            "Rossi",  # surname
            "mario.rossi@example.com",  # email
            "M",  # gender
            "1990-01-01",  # birthdate
            "single",  # civil_status
            interests  # interest_list
        )]
        self.mock_connection.query.return_value = mock_result
        
        # Execute the method to test
        result = self.repository.get_user_who_owns_sensor(test_sensor_uuid)
        
        # Verify the results
        self.assertIsNotNone(result)
        self.assertEqual(result.user_uuid, test_user_uuid)
        self.assertEqual(result.assigned_sensor_uuid, test_sensor_uuid)
        self.assertEqual(result.interests, interests)
        
        # Verify that the query is executed with the correct parameters
        self.mock_connection.query.assert_called_once()
        call_args = self.mock_connection.query.call_args
        self.assertIn("parameters", call_args[1])
        self.assertEqual(call_args[1]["parameters"]["sensor_uuid"], test_sensor_uuid)

    def test_get_user_who_owns_sensor_not_found(self):
        # Prepare mock to simulate no user found
        mock_result = Mock()
        mock_result.result_rows = []
        self.mock_connection.query.return_value = mock_result
        test_sensor_uuid = uuid.uuid4()
        
        # Execute the method to test
        result = self.repository.get_user_who_owns_sensor(test_sensor_uuid)
        
        # Verify the results
        self.assertIsNone(result)


