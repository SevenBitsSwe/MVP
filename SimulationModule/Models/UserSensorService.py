from Models.UserRepository import UserRepository
from Models.SensorRepository import SensorRepository
from Models.UserDAO import UserDAO
from Models.SensorDAO import SensorDAO
import uuid
import threading

class UserSensorService:

    def __init__(self):
        self.__SensorRepository = SensorRepository()
        self.__UserRepository = UserRepository()
        self.__lock = threading.Lock()  # Add a lock object

    def assign_sensor_to_user(self) -> uuid:
        """Assigns a sensor to a user"""
        with self.__lock:  # Use a context manager to acquire and release the lock
            sensor = self.__SensorRepository.get_non_occupied_sensor()

            user = self.__UserRepository.get_free_user()

            if not sensor or not user:
                return None
            
            self.__SensorRepository.mark_sensor_as_occupied(sensor._sensor_uuid)

            self.__UserRepository.mark_user_as_occupied(user._user_uuid, sensor._sensor_uuid)

            return sensor._sensor_uuid