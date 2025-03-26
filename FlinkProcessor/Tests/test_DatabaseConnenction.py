import unittest
from Core.DatabaseConnection import DatabaseConnection
from Core.DatabaseConfigParameters import DatabaseConfigParameters
import clickhouse_connect
from unittest.mock import MagicMock,patch
from Core.DatabaseConfigParameters import DatabaseConfigParameters

#TU5
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
        """Test that verifies error handling during connection"""
        # Configure mock to raise an exception
        mock_get_client.side_effect = Exception("Connection error")

        # Verify that an exception is raised
        with self.assertRaises(Exception):
            self.db_connection.connect()

        # Verify that the connection was not set
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



class TestKafkaConfigParameters(unittest.TestCase):

    def test_default_values(self):
        config = DatabaseConfigParameters()
        self.assertEqual("clickhouse", config.host)
        self.assertEqual("8123", config.port)
        self.assertEqual("default", config.user)
        self.assertEqual("pass", config.password)
