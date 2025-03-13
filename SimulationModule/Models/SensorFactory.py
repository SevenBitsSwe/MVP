from Models.SensorSubject import SensorSubject
from Models.GpsSensor import GpsSensor
from Models.UserSensorService import UserSensorService
from Models.ISensorRepository import ISensorRepository
from Models.IUserRepository import IUserRepository
from Models.IPositionSimulationStrategy import IPositionSimulationStrategy
from Models.PositionSender import PositionSender


class SensorFactory:

    # @classmethod
    # def initialize(cls, sensor_repo: SensorRepository, user_repo: UserRepository):
    #     cls.__user_sensor_service = UserSensorService(sensor_repo, user_repo)

    def __init__(self, sensor_repo: ISensorRepository, user_repo: IUserRepository):
        self.__user_sensor_service = UserSensorService(sensor_repo, user_repo)

    def create_gps_sensor(self, position_sender: PositionSender, simulation_strategy: IPositionSimulationStrategy) -> SensorSubject:
        '''method to create the GPS sensor'''
        uuid = self.__user_sensor_service.assign_sensor_to_user()
        return GpsSensor(uuid, position_sender, simulation_strategy)
        # return GpsSensor(cls.__user_sensor_service.assign_sensor_to_user())

    def create_gps_sensor_list(self, position_sender: PositionSender, simulation_strategy: IPositionSimulationStrategy, number_of_sensors: int) -> list[SensorSubject]:
        sensor_list = [self.create_gps_sensor(position_sender, simulation_strategy) for i in range(number_of_sensors)]
        return sensor_list
        
    
