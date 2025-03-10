from Models.SensorSubject import SensorSubject
from Models.GpsSensor import GpsSensor
from Models.UserSensorService import UserSensorService
from Models.SensorRepository import SensorRepository
from Models.UserRepository import UserRepository
import uuid

class SensorFactory:

    # @classmethod
    # def initialize(cls, sensor_repo: SensorRepository, user_repo: UserRepository):
    #     cls.__user_sensor_service = UserSensorService(sensor_repo, user_repo)

    def __init__(self, sensor_repo: SensorRepository, user_repo: UserRepository):
        self.__user_sensor_service = UserSensorService(sensor_repo, user_repo)

    def create_gps_sensor(cls) -> SensorSubject:
        '''method to create the GPS sensor'''
        uuid = cls.__user_sensor_service.assign_sensor_to_user()
        return GpsSensor(uuid)
        # return GpsSensor(cls.__user_sensor_service.assign_sensor_to_user())
    