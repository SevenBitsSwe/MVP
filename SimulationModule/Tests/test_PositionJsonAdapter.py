import unittest
from unittest.mock import MagicMock
import uuid
from Models.IJsonSerializable import IJsonSerializable
from Models.PositionJsonAdapter import PositionJsonAdapter
from Models.GeoPosition import GeoPosition

class TestPositionJsonAdapter(unittest.TestCase):
    def setUp(self):
        self.adapter = PositionJsonAdapter()
        self.mock_position = MagicMock(spec = GeoPosition)
        self.mock_position.get_sensor_id.return_value = "test_id"
        self.mock_position.get_latitude.return_value = 0.0  
        self.mock_position.get_longitude.return_value = 0.0
        self.mock_position.get_timestamp.return_value = "2025-03-05 14:30:00"

    def test_serialize_to_json(self):
        json_position = self.adapter.serialize_to_json(self.mock_position)
        self.assertEqual(json_position, '{"user_uuid": "test_id", "latitude": 0.0, "longitude": 0.0, "received_at": "2025-03-05 14:30:00"}')
