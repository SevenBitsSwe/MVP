import unittest
from unittest.mock import MagicMock
import uuid
from Models.IPositionObserver import IPositionObserver
from Models.GeoPosition import GeoPosition
from Models.GpsSensor import GpsSensor

class TestGpsSensor(unittest.TestCase):
    def setUp(self):
        self.test_uuid = uuid.uuid4()
        self.test_sensor = GpsSensor(self.test_uuid)
        self.mock_observer = MagicMock(spec = IPositionObserver)
    
    def test_init(self):
        self.assertEqual(self.test_sensor._sensor_uuid, self.test_uuid)
        self.assertEqual(self.test_sensor._observers_list, [])
        self.assertIsNone(self.test_sensor._GpsSensor__currentPosition)

    def test_register_observer(self):
        self.test_sensor.register_observer(self.mock_observer)
        self.assertIn(self.mock_observer, self.test_sensor._observers_list)
        self.assertEqual(len(self.test_sensor._observers_list), 1)

    def test_unregister_observer(self):
        self.test_sensor.register_observer(self.mock_observer)
        self.test_sensor.unregister_observer(self.mock_observer)
        self.assertNotIn(self.mock_observer, self.test_sensor._observers_list)
        self.assertEqual(len(self.test_sensor._observers_list), 0)
    
    def test_notify_observers(self):
        self.test_sensor.register_observer(self.mock_observer)
        self.test_sensor.notify_observers()
        self.mock_observer.on_sensor_data_changed.assert_called_once_with(self.test_sensor)

    def test_get_current_data(self):
        self.assertIsNone(self.test_sensor.get_current_data())
        position = MagicMock(spec = GeoPosition)
        self.test_sensor.set_current_position(position)
        self.assertEqual(self.test_sensor.get_current_data(), position)

    def test_set_current_position(self):
        position = MagicMock(spec = GeoPosition)
        self.test_sensor.register_observer(self.mock_observer)
        self.test_sensor.set_current_position(position)
        self.assertEqual(self.test_sensor._GpsSensor__currentPosition, position)
        self.mock_observer.on_sensor_data_changed.assert_called_once_with(self.test_sensor)

    def test_get_sensor_uuid(self):
        self.assertEqual(self.test_sensor.get_sensor_uuid(), self.test_uuid)