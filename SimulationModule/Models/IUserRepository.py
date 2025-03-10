from Models.UserDAO import UserDAO
from Models.DatabaseConfig import DatabaseConfig
from abc import ABC, abstractmethod
import uuid

class IUserRepository(ABC):
    @abstractmethod
    def connect(self, db_config: DatabaseConfig):
        pass

    @abstractmethod
    def mark_user_as_occupied(self, user_uuid: uuid.UUID, sensor_uuid: uuid.UUID):
        pass

    @abstractmethod
    def get_free_user(self) -> UserDAO:
        pass