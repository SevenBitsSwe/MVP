from Models.UserRepository import UserRepository
from Models.SensorRepository import SensorRepository
from Models.UserDAO import UserDAO
from Models.SensorDAO import SensorDAO
import uuid
import threading

class UserSensorService:

    def __init__(self, sensor_repository: SensorRepository, user_repository: UserRepository):
        self.__SensorRepository = sensor_repository
        self.__UserRepository = user_repository
        self.__lock = threading.Lock()  # Add a lock object

    def assign_sensor_to_user(self) -> uuid:
        """Assigns a sensor to a user"""
        with open('sensor_assignment.log', 'a') as log_file:
            log_file.write("Starting sensor assignment process...\n")
            with self.__lock:  # Use a context manager to acquire and release the lock
                log_file.write("Lock acquired\n")
                sensor = self.__SensorRepository.get_non_occupied_sensor()
                log_file.write(f"Found sensor: {sensor._sensor_uuid if sensor else 'None'}\n")

                user = self.__UserRepository.get_free_user()
                log_file.write(f"Found user: {user._user_uuid if user else 'None'}\n")

                if not sensor or not user:
                    log_file.write("Assignment failed: no available sensor or user\n")
                    return None
                
                self.__SensorRepository.mark_sensor_as_occupied(sensor._sensor_uuid)
                log_file.write(f"Marked sensor {sensor._sensor_uuid} as occupied\n")

                self.__UserRepository.mark_user_as_occupied(user._user_uuid, sensor._sensor_uuid)
                log_file.write(f"Assigned sensor {sensor._sensor_uuid} to user {user._user_uuid}\n")

                return sensor._sensor_uuid