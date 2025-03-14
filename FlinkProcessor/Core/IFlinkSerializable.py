from abc import ABC, abstractmethod
from pyflink.common import Types
from pyflink.common.types import Row


class IMessageRepository(ABC):
    '''Interface class which represent the ability to be serialized as a flink Row'''
    @abstractmethod
    def to_row(self) -> Row:
        pass