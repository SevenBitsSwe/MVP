import unittest
from unittest.mock import MagicMock,patch
from Models.DatabaseConnection import DatabaseConnection
from Models.DatabaseConfigParameters import DatabaseConfigParameters

class TestDatabaseConnection(unittest.TestCase):

    def setUp(self):
        self.config_parameters = DatabaseConfigParameters()

        self.db_connection = DatabaseConnection(self.config_parameters)

    @patch('clickhouse_connect.get_client')
    def test_connect(self, mock_get_client):
        mock_client_instance = MagicMock()
        mock_client_instance = mock_get_client.return_value

        result = self.db_connection.connect()

        mock_get_client.assert_called_once_with(
            host=self.config_parameters.host,
            port=self.config_parameters.port,
            username=self.config_parameters.user,
            password=self.config_parameters.password
        )
        self.assertEqual(result, mock_client_instance)
        self.assertEqual(self.db_connection.connection, mock_client_instance)

    @patch('clickhouse_connect.get_client')
    def test_connect_failure(self, mock_get_client):
        """Test to verify connection error management"""
        # Configure the mock to raise an exception
        mock_get_client.side_effect = Exception("Errore di connessione")

        # Verify that an exception is raised
        with self.assertRaises(Exception):
            self.db_connection.connect()

        # Verify the connection
        self.assertIsNone(self.db_connection.connection)

    def test_disconnect_success(self):
        mock_client_instance = MagicMock()
        self.db_connection.connection = mock_client_instance

        self.db_connection.disconnect()

        mock_client_instance.close.assert_called_once()

        self.assertIsNone(self.db_connection.connection)

    def test_disconnect_no_connection(self):
        self.db_connection.connection = None

        self.db_connection.disconnect()

        self.assertIsNone(self.db_connection.connection)
