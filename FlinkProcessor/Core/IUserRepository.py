from Core.UserDTO import UserDTO
from Core.DatabaseConnection import DatabaseConnection
from abc import ABC, abstractmethod
import uuid

class IUserRepository(ABC):
    @abstractmethod
    def get_user_who_owns_sensor(self, sensor_uuid) -> UserDTO:
        pass
    
