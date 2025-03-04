import unittest
from unittest.mock import MagicMock
import uuid
from Models.IPositionObserver import IPositionObserver
from Models.GpsSensor import GpsSensor

class TestSensorSubject(unittest.TestCase):
    def setUp(self):
        self.test_uuid = uuid.uuid4()
        self.test_sensor = GpsSensor(self.test_uuid)
        self.mock_observer = MagicMock(spec = IPositionObserver)
    
    def test_init(self):
        self.assertEqual(self.test_sensor._sensor_uuid, self.test_uuid)
        self.assertEqual(self.test_sensor._observers_list, [])

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
        self.test_sensor.notify_observers(self.test_sensor)
        self.mock_observer.on_sensor_data_changed.assert_called_once_with(self.test_sensor)

    