from abc import ABC, abstractmethod
from Core.MessageDTO import MessageDTO

class IMessageRepository(ABC):
    @abstractmethod
    def get_user_last_message(self, user_id : str) -> MessageDTO:
        pass
