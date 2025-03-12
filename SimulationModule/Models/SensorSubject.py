'''This module contains the SensorSubject class, which is a subject class 
for the Observer pattern. It is used to abstract the sensor and make it 
observable by the Observer classes. It is used to notify the Observer
classes when the sensor data changes.'''

from abc import ABC, abstractmethod
import uuid

class SensorSubject(ABC):
    '''Abstract Class implementation '''

    def __init__(self, uuid_creation: uuid):
        '''constructor to initialize the sensor subject'''
        self._sensor_uuid = uuid_creation

    def get_sensor_uuid(self):
        '''method to get the sensor uuid'''
        return self._sensor_uuid
    
    @abstractmethod
    def simulate(self):
        '''abstract method to get the current data'''
        pass
    
