from Models.IUserRepository import IUserRepository
from Models.ISensorRepository import ISensorRepository
from Models.UserDTO import UserDTO
from Models.SensorDTO import SensorDTO
import uuid
import threading
import time

class UserSensorService:

    def __init__(self, sensor_repository: ISensorRepository, user_repository: IUserRepository):
        self.__SensorRepository = sensor_repository
        self.__UserRepository = user_repository
        self.__lock = threading.Lock()  # Add a lock object

    def assign_sensor_to_user(self) -> uuid:
        """Assigns a sensor to a user"""
        with open('sensor_assignment.log', 'a') as log_file:
            log_file.write("Starting sensor assignment process...\n")
            time.sleep(1)
            with self.__lock:  # Use a context manager to acquire and release the lock
                log_file.write("Lock acquired\n")
                sensor = self.__SensorRepository.get_non_occupied_sensor()
                log_file.write(f"Found sensor: {sensor.sensor_uuid if sensor else 'None'}\n")

                user = self.__UserRepository.get_free_user()
                log_file.write(f"Found user: {user.user_uuid if user else 'None'}\n")

                if not sensor or not user:
                    log_file.write("Assignment failed: no available sensor or user\n")
                    return None
                
                self.__SensorRepository.mark_sensor_as_occupied(sensor.sensor_uuid)
                log_file.write(f"Marked sensor {sensor.sensor_uuid} as occupied\n")

                self.__UserRepository.mark_user_as_occupied(user.user_uuid, sensor.sensor_uuid)
                log_file.write(f"Assigned sensor {sensor.sensor_uuid} to user {user.user_uuid}\n")

                return sensor.sensor_uuid
