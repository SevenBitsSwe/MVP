import unittest
from unittest.mock import MagicMock
import uuid
from Models.GeoPosition import GeoPosition

class TestGeoPosition(unittest.TestCase):
    
    def setUp(self):
        self.test_sensor_id = str(uuid.uuid4())
        self.test_latitude = 0.0
        self.test_longitude = 0.0
        self.test_timestamp = "2025-03-05 14:30:00"
        self.test_geo_position = GeoPosition(self.test_sensor_id, self.test_latitude, self.test_longitude, self.test_timestamp)

    def test_init(self):
        self.assertEqual(self.test_geo_position._GeoPosition__sensor_id, self.test_sensor_id)
        self.assertEqual(self.test_geo_position._GeoPosition__latitude, self.test_latitude)
        self.assertEqual(self.test_geo_position._GeoPosition__longitude, self.test_longitude)
        self.assertEqual(self.test_geo_position._GeoPosition__timestamp, self.test_timestamp)

    def test_get_sensor_id(self):
        self.assertEqual(self.test_geo_position.get_sensor_id(), self.test_sensor_id)

    def test_get_latitude(self):
        self.assertEqual(self.test_geo_position.get_latitude(), self.test_latitude)

    def test_get_longitude(self):
        self.assertEqual(self.test_geo_position.get_longitude(), self.test_longitude)

    def test_get_timestamp(self):
        self.assertEqual(self.test_geo_position.get_timestamp(), self.test_timestamp)