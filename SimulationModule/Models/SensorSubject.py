'''This module contains the SensorSubject class, which is a subject class 
for the Observer pattern. It is used to abstract the sensor and make it 
observable by the Observer classes. It is used to notify the Observer
classes when the sensor data changes.'''

from abc import ABC, abstractmethod
import uuid


class SensorSubject(ABC):
    '''Abstract Class implementation '''

    def __init__(self, uuid_creation: uuid, simulation_strategy: "IPositionSimulationStrategy"):
        '''constructor to initialize the sensor subject'''
        self._sensor_uuid = uuid_creation
        self._simulation_strategy = simulation_strategy
        self._update_time = simulation_strategy.get_delta_time()

    def get_sensor_uuid(self):
        '''method to get the sensor uuid'''
        return self._sensor_uuid

    def get_update_time(self) -> float:
        return self._update_time

    @abstractmethod
    def simulate(self):
        '''abstract method to get the current data'''
        pass
