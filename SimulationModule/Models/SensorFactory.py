from Models.SensorSubject import SensorSubject
from Models.GpsSensor import GpsSensor
from Models.UserSensorService import UserSensorService
import uuid

class SensorFactory:
    __user_sensor_service = UserSensorService()

    @classmethod
    def create_gps_sensor(cls) -> SensorSubject:
        '''method to create the GPS sensor'''
        uuid = cls.__user_sensor_service.assign_sensor_to_user()
        return GpsSensor(uuid)
        # return GpsSensor(cls.__user_sensor_service.assign_sensor_to_user())
    