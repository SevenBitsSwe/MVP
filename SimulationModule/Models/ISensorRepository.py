from abc import ABC, abstractmethod

class ISensorRepository(ABC):
    @abstractmethod
    def connect(self):
        pass