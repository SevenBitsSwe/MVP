import unittest
from Models.SensorSubject import SensorSubject
from Models.GpsSensor import GpsSensor
from Models.UserSensorService import UserSensorService
from Models.ISensorRepository import ISensorRepository
from Models.IUserRepository import IUserRepository
from Models.SensorFactory import SensorFactory
from Models.PositionSender import PositionSender
from Models.IPositionSimulationStrategy import IPositionSimulationStrategy
from unittest.mock import Mock, patch
import uuid

# TU27
class TestSensorFactory(unittest.TestCase):
    def setUp(self):
        self.mock_sensor_repository = Mock(spec=ISensorRepository)
        self.mock_user_repository = Mock(spec=IUserRepository)
        self.mock_position_sender = Mock(spec=PositionSender)
        self.mock_simulation_strategy = Mock(spec=IPositionSimulationStrategy)
        self.mock_user_sensor_service=Mock(spec=UserSensorService)

        self.patcher = patch('Models.SensorFactory.UserSensorService', return_value=self.mock_user_sensor_service)
        self.patcher.start()

        self.sensor_factory = SensorFactory(self.mock_sensor_repository, self.mock_user_repository)
        
    def tearDown(self):
        # it stops the patcher after every test
        self.patcher.stop()

    def test_create_gps_sensor_correct_type(self):
        mock_uuid = uuid.uuid4()
        self.mock_user_sensor_service.assign_sensor_to_user.return_value = mock_uuid

        sensor_instance = self.sensor_factory.create_gps_sensor(self.mock_position_sender, self.mock_simulation_strategy)
        self.assertIsInstance(sensor_instance, SensorSubject)
        self.assertIsInstance(sensor_instance, GpsSensor)
    
    def test_create_gps_sensor_valid_uuid(self):
        mock_uuid = uuid.uuid4()
        self.mock_user_sensor_service.assign_sensor_to_user.return_value = mock_uuid
        sensor_instance = self.sensor_factory.create_gps_sensor(self.mock_position_sender, self.mock_simulation_strategy)
        self.assertIsNotNone(sensor_instance.get_sensor_uuid())
        sensor_uuid = sensor_instance.get_sensor_uuid()

        self.assertEqual(str(sensor_uuid), str(mock_uuid))
        
    
    def test_sensor_has_unique_uuid(self):
        num_sensor = 10
        mock_uuids = [f"mock-uuid-{i}" for i in range(num_sensor)]
        self.mock_user_sensor_service.assign_sensor_to_user.side_effect = mock_uuids

        sensors_list = [self.sensor_factory.create_gps_sensor(self.mock_position_sender, self.mock_simulation_strategy) for _ in range(num_sensor)]
        sensors_uuid_list = [sensor.get_sensor_uuid() for sensor in sensors_list]
        #set contains only different elements, so if len corresponds it means they are unique
        self.assertEqual(len(sensors_uuid_list), len(set(sensors_uuid_list)))

    def test_create_gps_sensor_list(self):
        num_sensors = 5
        mock_uuids = [uuid.uuid4() for _ in range(num_sensors)]
        self.mock_user_sensor_service.assign_sensor_to_user.side_effect = mock_uuids

        sensors_list = self.sensor_factory.create_gps_sensor_list(self.mock_position_sender, self.mock_simulation_strategy, num_sensors)
        
        self.assertEqual(len(sensors_list), num_sensors)
        
        for sensor in sensors_list:
            self.assertIsInstance(sensor, GpsSensor)
