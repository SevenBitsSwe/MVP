from abc import ABC, abstractmethod

class IUserRepository(ABC):
    @abstractmethod
    def connect(self):
        pass