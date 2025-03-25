from abc import ABC, abstractmethod
from Core.UserDTO import UserDTO

class IUserRepository(ABC):
    @abstractmethod
    def get_user_who_owns_sensor(self, sensor_uuid) -> UserDTO:
        pass
