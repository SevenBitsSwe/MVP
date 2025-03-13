from Core.UserDTO import UserDTO
from Core.DatabaseConnection import DatabaseConnection
from abc import ABC, abstractmethod
import uuid

class IUserRepository(ABC):
    @abstractmethod
    def mark_user_as_occupied(self, user_uuid: uuid.UUID, sensor_uuid: uuid.UUID):
        pass

    @abstractmethod
    def get_free_user(self) -> UserDTO:
        pass
    @abstractmethod
    def get_user_who_owns_sensor(self, sensor_uuid) -> UserDTO:
        pass
    