from abc import ABC, abstractmethod
from Models.SensorSubject import SensorSubject

class IPositionObserver(ABC):
    '''Interface class for the observer that observes the position retrieved by the GPS sensor'''

    @abstractmethod
    def on_sensor_data_changed(self, sensor_istance: SensorSubject):
        '''abstract method to be implemented by the observer'''
        pass