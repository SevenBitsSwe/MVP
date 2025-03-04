from Models.SensorSubject import SensorSubject
from Models.GeoPosition import GeoPosition

class GpsSensor(SensorSubject):
    '''This class inherit from the SensorSubject class and implements the GPS sensor '''

    def __init__(self):
        '''constructor to initialize the GPS sensor'''
        super().__init__()
        self.__currentPosition = None
        
    def get_current_data(self) -> "GpsSensor":
        '''method to get the current position'''
        return self.__currentPosition

    def set_current_position(self, position_istance: GeoPosition):
        '''method to set the current position'''
        self.__currentPosition = position_istance
        self.notify_observers() 
        
    def get_sensor_uuid(self):
        '''method to get the sensor uuid'''
        return self._sensor_uuid
    