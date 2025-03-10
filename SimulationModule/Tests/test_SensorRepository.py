import unittest
from Models.SensorRepository import SensorRepository
from Models.ISensorRepository import ISensorRepository
from Models.DatabaseConnection import DatabaseConnection
from Models.SensorDTO import SensorDTO
import uuid
from unittest.mock import Mock

class TestSensorRepository(unittest.TestCase):

    def setUp(self):
        self.mock_db_connection = Mock(spec=DatabaseConnection)

        self.sensor_repository = SensorRepository(self.mock_db_connection)

    def test_mark_sensor_as_occupied(self):
        mock_conn = Mock()
        self.mock_db_connection.connect.return_value = mock_conn

        test_uuid = uuid.uuid4()

        self.sensor_repository.mark_sensor_as_occupied(test_uuid)

        self.mock_db_connection.connect.assert_called_once()
        self.mock_db_connection.disconnect.assert_called_once()

        expected_query = f"ALTER TABLE nearyou.sensor UPDATE is_occupied = true WHERE sensor_uuid = '{test_uuid}'"
        mock_conn.query.assert_called_once_with(expected_query)

    def test_get_non_occupied_sensor(self):
        mock_conn = Mock()
        self.mock_db_connection.connect.return_value = mock_conn

        test_uuid = uuid.uuid4()

        self.sensor_repository.mark_sensor_as_occupied(test_uuid)

        result = self.sensor_repository.get_non_occupied_sensor()

        self.mock_db_connection.connect.assert_called_once()
        self.mock_db_connection.disconnect.assert_called_once()

        expected_query = "SELECT sensor_uuid, is_occupied FROM nearyou.sensor WHERE is_occupied = 0"
        mock_conn.query.assert_called_once_with(expected_query)

        self.assertIsInstance(result, SensorDTO)
        self.assertEqual(result.sensor_uuid, test_uuid)
        self.assertFalse(result.is_occupied)

    def test_get_non_occupied_sensor_no_results(self):
        mock_conn = Mock()
        self.mock_db_connection.connect.return_value = mock_conn

        mock_conn.query.return_value.result_rows = []

        result = self.sensor_repository.get_non_occupied_sensor()

        self.mock_db_connection.connect.assert_called_once()
        self.mock_db_connection.disconnect.assert_called_once()

        expected_query = "SELECT sensor_uuid, is_occupied FROM nearyou.sensor WHERE is_occupied = 0"
        mock_conn.query.assert_called_once_with(expected_query)

        self.assertIsNone(result)
