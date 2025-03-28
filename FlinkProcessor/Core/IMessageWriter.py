from abc import ABC, abstractmethod

class IMessageWriter(ABC):
    '''Interface class which represent the outbound port, also known as the message writer'''
    @abstractmethod
    def get_message_writer(self):
        pass
