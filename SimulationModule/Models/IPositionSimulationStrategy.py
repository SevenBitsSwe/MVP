from abc import ABC, abstractmethod


class IPositionSimulationStrategy(ABC):
    '''Implementation of the pattern strategy to abastract different ways of generating random data'''
    @abstractmethod
    def get_route(self) -> list:
        '''abstract method to simulate the position live update'''
        pass

    @abstractmethod
    def get_delta_time(self) -> float:
        pass

    @abstractmethod
    def get_speed(self) -> float:
        pass
