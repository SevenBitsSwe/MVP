from abc import ABC, abstractmethod

class IPositionReceiver(ABC):
    '''Interface class which represent the inbound port, also known as the position receiver'''
    @abstractmethod
    def get_position_receiver(self):
        pass