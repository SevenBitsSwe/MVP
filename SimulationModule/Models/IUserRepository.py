from abc import ABC, abstractmethod
import uuid
from Models.UserDAO import UserDAO

class IUserRepository(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def mark_user_as_occupied(self, user_uuid: uuid.UUID, sensor_uuid: uuid.UUID):
        pass

    @abstractmethod
    def get_free_user(self) -> UserDAO:
        pass