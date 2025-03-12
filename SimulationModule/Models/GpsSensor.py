from Models.SensorSubject import SensorSubject
from Models.GeoPosition import GeoPosition
import uuid
class GpsSensor(SensorSubject):
    '''This class inherit from the SensorSubject class and implements the GPS sensor '''

    def __init__(self,uuid_creation: uuid):
        '''constructor to initialize the GPS sensor'''
        super().__init__(uuid_creation)
        
    def simulate(self):
        '''method to get the current position'''
        self.create_geo_position()

    def create_geo_position(self):
        '''method to set the current position'''
        pass
        
    
    
