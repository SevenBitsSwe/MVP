from Core.MessageDTO import MessageDTO
from Core.DatabaseConnection import DatabaseConnection
from abc import ABC, abstractmethod
import uuid

class IMessageRepository(ABC):
    @abstractmethod
    def get_user_last_message(self,user_id) -> dict:
        pass


        