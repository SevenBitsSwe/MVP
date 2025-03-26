import unittest
from unittest.mock import Mock
from Models.UserSensorService import UserSensorService
from Models.IUserRepository import IUserRepository
from Models.ISensorRepository import ISensorRepository
from Models.UserDTO import UserDTO
from Models.SensorDTO import SensorDTO
import uuid

# TU31
class TestUserSensorService(unittest.TestCase):

    def setUp(self):
        self.mock_sensor_repository = Mock(spec=ISensorRepository)
        self.mock_user_repository = Mock(spec=IUserRepository)

        self.user_sensor_service = UserSensorService(self.mock_sensor_repository, self.mock_user_repository)
        
    def test_assign_sensor_to_user_success(self):
        test_sensor_uuid = uuid.uuid4()
        test_user_uuid = uuid.uuid4()

        mock_sensor = Mock(spec=SensorDTO)
        mock_sensor.sensor_uuid = test_sensor_uuid

        mock_user = Mock(spec=UserDTO)
        mock_user.user_uuid = test_user_uuid

        self.mock_sensor_repository.get_non_occupied_sensor.return_value = mock_sensor
        self.mock_user_repository.get_free_user.return_value = mock_user

        result = self.user_sensor_service.assign_sensor_to_user()

        self.mock_sensor_repository.get_non_occupied_sensor.assert_called_once()
        self.mock_user_repository.get_free_user.assert_called_once()
        self.mock_sensor_repository.mark_sensor_as_occupied.assert_called_once_with(test_sensor_uuid)
        self.mock_user_repository.mark_user_as_occupied.assert_called_once_with(test_user_uuid, test_sensor_uuid)

        self.assertEqual(result, test_sensor_uuid)

    def test_assign_sensor_to_user_no_sensor_available(self):
        self.mock_sensor_repository.get_non_occupied_sensor.return_value = None

        test_user_uuid = uuid.uuid4()
        mock_user = Mock(spec=UserDTO)
        mock_user.user_uuid = test_user_uuid
        self.mock_user_repository.get_free_user.return_value = mock_user

        result = self.user_sensor_service.assign_sensor_to_user()

        self.mock_sensor_repository.get_non_occupied_sensor.assert_called_once()
        self.mock_user_repository.get_free_user.assert_called_once()

        self.assertIsNone(result)

    def test_assign_sensor_to_user_no_user_available(self):
        test_sensor_uuid = uuid.uuid4()
        mock_sensor = Mock(spec=SensorDTO)
        mock_sensor.sensor_uuid = test_sensor_uuid
        self.mock_sensor_repository.get_non_occupied_sensor.return_value = mock_sensor

        self.mock_user_repository.get_free_user.return_value = None

        result = self.user_sensor_service.assign_sensor_to_user()

        self.mock_sensor_repository.get_non_occupied_sensor.assert_called_once()
        self.mock_user_repository.get_free_user.assert_called_once()

        self.assertIsNone(result)

    def test_assign_sensor_to_user_no_sensor_and_no_user_available(self):
        self.mock_sensor_repository.get_non_occupied_sensor.return_value = None
        self.mock_user_repository.get_free_user.return_value = None

        result = self.user_sensor_service.assign_sensor_to_user()

        self.mock_sensor_repository.get_non_occupied_sensor.assert_called_once()
        self.mock_user_repository.get_free_user.assert_called_once()

        self.assertIsNone(result)
