from abc import ABC, abstractmethod

class IMessageRepository(ABC):
    @abstractmethod
    def check_activity_already_displayed_for_user(self, user_id : str,activity_id : str) -> bool:
        pass
