from Models.UserDTO import UserDTO
from Models.DatabaseConnection import DatabaseConnection
from abc import ABC, abstractmethod
import uuid

class IUserRepository(ABC):
    @abstractmethod
    def mark_user_as_occupied(self, user_uuid: uuid.UUID, sensor_uuid: uuid.UUID):
        pass

    @abstractmethod
    def get_free_user(self) -> UserDTO:
        pass
