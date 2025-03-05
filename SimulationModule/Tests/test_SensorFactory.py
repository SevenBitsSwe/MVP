import unittest
from Models.SensorSubject import SensorSubject
from Models.GpsSensor import GpsSensor
from Models.SensorFactory import SensorFactory
import uuid 

class TestSensorFactory(unittest.TestCase):
    def test_create_gps_sensor_correct_type(self):
        sensor_istance = SensorFactory.create_gps_sensor()
        self.assertIsInstance(sensor_istance, SensorSubject)
        self.assertIsInstance(sensor_istance, GpsSensor)
    
    def test_create_gps_sensor_valid_uuid(self):
        sensor_istance = SensorFactory.create_gps_sensor()
        self.assertIsNotNone(sensor_istance.get_sensor_uuid())
        sensor_uuid = sensor_istance.get_sensor_uuid()

        uuid_obj = uuid.UUID(str(sensor_uuid))
        self.assertEqual(str(sensor_uuid), str(uuid_obj))
        
    
    def test_sensor_has_unique_uuid(self):
        num_sensor = 10
        sensors_list = [SensorFactory.create_gps_sensor() for _ in range(num_sensor)]
        sensors_uuid_list = [sensor.get_sensor_uuid() for sensor in sensors_list]
        #set contains only different elements, so if len corresponds it means they are unique
        self.assertEqual(len(sensors_uuid_list), len(set(sensors_uuid_list)))