from Models.SensorSubject import SensorSubject
from Models.GeoPosition import GeoPosition
import uuid
class GpsSensor(SensorSubject):
    '''This class inherit from the SensorSubject class and implements the GPS sensor '''

    def __init__(self,uuid_creation: uuid):
        '''constructor to initialize the GPS sensor'''
        super().__init__(uuid_creation)
        self.__currentPosition = None
        
    def notify_observers(self,sensor_istance: "GpsSensor"):
        '''method to notify the observers'''
        for observer in self._observers_list:
            observer.on_sensor_data_changed(sensor_istance)

    def get_current_data(self):
        '''method to get the current position'''
        return self.__currentPosition

    def set_current_position(self, position_istance: GeoPosition):
        '''method to set the current position'''
        self.__currentPosition = position_istance
        self.notify_observers(self) 
        
    
    