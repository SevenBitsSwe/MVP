from abc import abstractmethod, ABC
from pyflink.common.types import Row
from Core.MessageDTO import MessageDTO

class IFlinkSerializable(ABC):
    '''Interface class which represents the inbound port, also known as the position receiver'''
    @abstractmethod
    def create_row_from_message(self,message_to_serialize: MessageDTO) -> Row:
        pass
