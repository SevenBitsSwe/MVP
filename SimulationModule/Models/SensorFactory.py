from Models.SensorSubject import SensorSubject
from Models.GpsSensor import GpsSensor
import uuid

class SensorFactory:
    @classmethod
    def create_gps_sensor(self) -> SensorSubject:
        '''method to create the GPS sensor'''
        return GpsSensor(uuid.uuid4())