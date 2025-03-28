import unittest
from unittest.mock import Mock
import uuid
from Core.ClickhouseMessageRepository import ClickhouseMessageRepository
from Core.DatabaseConnection import DatabaseConnection
from Core.MessageDTO import MessageDTO

class TestClickhouseMessageRepository(unittest.TestCase):
    def setUp(self):
        # Create a mock for DatabaseConnection
        self.mock_db_connection = Mock(spec=DatabaseConnection)
        # Mock for connection result
        self.mock_connection = Mock()
        self.mock_db_connection.connect.return_value = self.mock_connection
        # Initialize the repository with the mock
        self.repository = ClickhouseMessageRepository(self.mock_db_connection)

    # def test_get_user_last_message_found(self):
    #     # Prepare test data
    #     test_user_id = uuid.uuid4()
    #     test_activity_id = uuid.uuid4()
    #     test_message_id = uuid.uuid4()

    #     # Create a mock for query result
    #     mock_result = Mock()
    #     mock_result.result_set = [{}]  # Necessary for length check
    #     mock_result.first_item = {
    #         'user_idd': str(test_user_id),
    #         'activity_id': str(test_activity_id),
    #         'message_id': str(test_message_id),
    #         'message_text': 'Ciao, sono vicino!',
    #         'latitude': '45.4642',
    #         'longitude': '9.1900',
    #         'creation_time': '2025-03-17 10:30:00',
    #         'user_lat': '45.4641',
    #         'user_lon': '9.1901'
    #     }

    #     self.mock_connection.query.return_value = mock_result

    #     # Execute the method to test
    #     result = self.repository.get_user_last_message(test_user_id)

    #     # Verify results
    #     self.assertEqual(result.user_id, str(test_user_id))
    #     self.assertEqual(result.activity_id, str(test_activity_id))
    #     self.assertEqual(result.message_id, str(test_message_id))
    #     self.assertEqual(result.message_text, 'Ciao, sono vicino!')
    #     self.assertEqual(result.activity_lat, 45.4642)
    #     self.assertEqual(result.activity_lon, 9.1900)
    #     self.assertEqual(result.creation_time, '2025-03-17 10:30:00')
    #     self.assertEqual(result.user_lat, 45.4641)
    #     self.assertEqual(result.user_lon, 9.1901)

    #     # Verify that the query is executed with correct parameters
    #     self.mock_connection.query.assert_called_once()
    #     call_args = self.mock_connection.query.call_args
    #     self.assertIn("parameters", call_args[1])
    #     self.assertEqual(call_args[1]["parameters"]["user_id"],test_user_id)

    # def test_get_user_last_message_not_found(self):
    #     # Prepare mock to simulate no message found
    #     test_user_id = uuid.uuid4()
    #     mock_result = Mock()
    #     mock_result.result_set = []  # No results found

    #     self.mock_connection.query.return_value = mock_result

    #     # Execute the method to test
    #     result = self.repository.get_user_last_message(test_user_id)

    #     # Verify that an empty MessageDTO is returned
    #     self.assertIsInstance(result, MessageDTO)
    #     self.assertEqual(result.user_lat, 0.0)
    #     self.assertEqual(result.user_lon, 0.0)

    #     # Verify that the query was executed with correct parameters
    #     self.mock_connection.query.assert_called_once()
    #     call_args = self.mock_connection.query.call_args
    #     self.assertEqual(call_args[1]["parameters"]["user_id"], test_user_id)
    def test_check_activity_already_displayed_for_user_found(self):
        """Verifica che il metodo restituisca True quando trova un messaggio per l'utente e l'attività specificati"""
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
