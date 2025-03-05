from abc import ABC, abstractmethod


class IPositionSimulationStrategy(ABC):
    '''Implementation of the pattern strategy to abastract different ways of generating random data'''
    @abstractmethod
    def simulate_position_live_update(self, sensor_istance: "SensorSubject"):
        '''abstract method to simulate the position live update'''
        pass
    