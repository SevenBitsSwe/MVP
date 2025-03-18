from Models.SensorSubject import SensorSubject
from Models.GeoPosition import GeoPosition
from Models.PositionSender import PositionSender
from Models.IPositionSimulationStrategy import IPositionSimulationStrategy
from geopy.distance import geodesic
import uuid
import time
from datetime import datetime

class GpsSensor(SensorSubject):
    '''This class inherit from the SensorSubject class and implements the GPS sensor '''

    def __init__(self,uuid_creation: uuid, position_sender: PositionSender, simulation_strategy: IPositionSimulationStrategy):
        '''constructor to initialize the GPS sensor'''
        super().__init__(uuid_creation,simulation_strategy)
        self.__position_sender = position_sender
        self.__speed_mps = simulation_strategy.get_speed()
        
    def simulate(self):
        route_coords = self._simulation_strategy.get_route()
        total_distance = 0
        for i in range(len(route_coords)-1):
            start_point = route_coords[i]
            end_point = route_coords[i+1]
            segment_distance = geodesic(start_point, end_point).meters
            total_distance += segment_distance
            num_positions = int(segment_distance / (self.__speed_mps * self._update_time))

            for j in range(num_positions):
                fraction = j / num_positions

                latitude = start_point[0] + fraction * (end_point[0] - start_point[0])
                longitude = start_point[1] + fraction * (end_point[1] - start_point[1])
                position = self.create_geo_position(latitude,longitude)
                self.__position_sender.send_position(position)
                time.sleep(self._update_time)

    def create_geo_position(self,latitude: float, longitude: float) -> GeoPosition:
        '''method to set the current position'''
        return GeoPosition(
            self._sensor_uuid,
            latitude,
            longitude,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        
    
    
