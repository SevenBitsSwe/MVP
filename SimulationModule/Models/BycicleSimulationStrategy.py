from Models.IPositionSimulationStrategy import IPositionSimulationStrategy
from Models.GpsSensor import GpsSensor
from Models.GeoPosition import GeoPosition
from datetime import datetime
import time

class BycicleSimulationStrategy(IPositionSimulationStrategy):
    def __init__(self):
        '''constructor to initialize the bycicle simulation strategy'''
        self.__bycicle_speed_approximated = 15
        self.__delta_time_between_positions = 5
        self.__dict_withStartingCoordinates = {'latitude': 45.464664, 'longitude': 9.188540}
    
    def simulate_position_live_update(self, sensor_istance: GpsSensor):
        '''method to simulate the position live update'''
        for i in range(10):
            time.sleep(self.__delta_time_between_positions)
            self.__dict_withStartingCoordinates['latitude'] += 0.0001
            self.__dict_withStartingCoordinates['longitude'] += 0.0001
            print("positiozne updated")
            sensor_istance.set_current_position(
                GeoPosition(
                    sensor_istance.get_sensor_uuid(),
                    self.__dict_withStartingCoordinates['latitude'],
                    self.__dict_withStartingCoordinates['longitude'],
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
            )
