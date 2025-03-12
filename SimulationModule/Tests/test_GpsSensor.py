import unittest
from unittest.mock import MagicMock
import uuid
from Models.GeoPosition import GeoPosition
from Models.GpsSensor import GpsSensor

class TestGpsSensor(unittest.TestCase):
    def setUp(self):
        self.test_uuid = uuid.uuid4()
        self.test_sensor = GpsSensor(self.test_uuid)
    
    def test_init(self):
        self.assertEqual(self.test_sensor._sensor_uuid, self.test_uuid)

    def test_simulate(self):
        pass

    def test_create_geo_position(self):
        pass

    def test_get_sensor_uuid(self):
        self.assertEqual(self.test_sensor.get_sensor_uuid(), self.test_uuid)
