import unittest
from unittest.mock import Mock
import uuid
from Core.ClickhouseMessageRepository import ClickhouseMessageRepository
from Core.DatabaseConnection import DatabaseConnection

class TestClickhouseMessageRepository(unittest.TestCase):
    def setUp(self):
        # Create a mock for DatabaseConnection
        self.mock_db_connection = Mock(spec=DatabaseConnection)
        # Mock for connection result
        self.mock_connection = Mock()
        self.mock_db_connection.connect.return_value = self.mock_connection
        # Initialize the repository with the mock
        self.repository = ClickhouseMessageRepository(self.mock_db_connection)

    def test_check_activity_already_displayed_for_user_found(self):
        """Verifies that the method returns True when it finds a message for the specified user and activity"""
        # Prepare test data
        test_user_id = str(uuid.uuid4())
        test_activity_id = str(uuid.uuid4())

        # Create a mock for query result with data (activity was displayed)
        mock_result = Mock()
        mock_result.result_set = [{'user_id': test_user_id, 'activity_id': test_activity_id}]

        self.mock_connection.query.return_value = mock_result

        # Execute the method to test
        result = self.repository.check_activity_already_displayed_for_user(test_user_id, test_activity_id)

        # Verify results
        self.assertTrue(result)

        # Verify that the query is executed with correct parameters
        self.mock_connection.query.assert_called_once()
        call_args = self.mock_connection.query.call_args
        self.assertIn("parameters", call_args[1])
        self.assertEqual(call_args[1]["parameters"]["user_id"], test_user_id)
        self.assertEqual(call_args[1]["parameters"]["activity_id"], test_activity_id)

    def test_check_activity_already_displayed_for_user_not_found(self):
        """Verifica che il metodo restituisca False quando non trova un messaggio per l'utente e l'attività specificati"""
        # Prepare test data
        test_user_id = str(uuid.uuid4())
        test_activity_id = str(uuid.uuid4())

        # Create a mock for query result with empty result (activity was not displayed)
        mock_result = Mock()
        mock_result.result_set = []

        self.mock_connection.query.return_value = mock_result

        # Execute the method to test
        result = self.repository.check_activity_already_displayed_for_user(test_user_id, test_activity_id)

        # Verify results
        self.assertFalse(result)

        # Verify that the query is executed with correct parameters
        self.mock_connection.query.assert_called_once()
        call_args = self.mock_connection.query.call_args
        self.assertIn("parameters", call_args[1])
        self.assertEqual(call_args[1]["parameters"]["user_id"], test_user_id)
        self.assertEqual(call_args[1]["parameters"]["activity_id"], test_activity_id)
