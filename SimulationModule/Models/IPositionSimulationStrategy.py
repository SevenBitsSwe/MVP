from abc import ABC, abstractmethod
from Models.GpsSensor import GpsSensor

class IPositionSimulationStrategy(ABC):
    '''Implementation of the pattern strategy to abastract different ways of generating random data'''
    @abstractmethod
    def simulate_position_live_update(self, sensor_istance: GpsSensor):
        '''abstract method to simulate the position live update'''
        pass
    