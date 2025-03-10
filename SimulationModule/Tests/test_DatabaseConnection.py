import unittest
from Models.DatabaseConnection import DatabaseConnection
from Models.DatabaseConfigParameters import DatabaseConfigParameters
import clickhouse_connect
from unittest.mock import MagicMock,patch

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
        """Test che verifica la gestione di un errore durante la connessione"""
        # Configura il mock per sollevare un'eccezione
        mock_get_client.side_effect = Exception("Errore di connessione")

        # Verifica che venga sollevata un'eccezione
        with self.assertRaises(Exception):
            self.db_connection.connect()

        # Verifica che la connessione non sia stata impostata
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

