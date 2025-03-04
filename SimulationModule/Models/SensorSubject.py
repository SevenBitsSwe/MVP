'''This module contains the SensorSubject class, which is a subject class 
for the Observer pattern. It is used to abstract the sensor and make it 
observable by the Observer classes. It is used to notify the Observer
classes when the sensor data changes.'''

from abc import ABC, abstractmethod
from Models.IPositionObserver import IPositionObserver
import uuid

class SensorSubject(ABC):
    '''Abstract Class implementation '''

    def __init__(self, uuid_creation: uuid):
        '''constructor to initialize the sensor subject'''
        self._sensor_uuid = uuid_creation
        self._observers_list = []

    def register_observer(self, observer_istance: IPositionObserver):
        '''method to register the observer'''
        self._observers_list.append(observer_istance)

    def unregister_observer(self, observer_istance: IPositionObserver):
        '''method to unregister the observer'''
        self._observers_list.remove(observer_istance)

    @abstractmethod
    def notify_observers(self, sensor_istance: "SensorSubject"):
        '''method to notify the observers'''
        pass

    @abstractmethod
    def get_current_data(self) -> "SensorSubject":
        '''abstract method to get the current data'''
        pass
    