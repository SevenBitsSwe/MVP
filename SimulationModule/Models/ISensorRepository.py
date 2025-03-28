import uuid
from abc import ABC, abstractmethod
from Models.SensorDTO import SensorDTO

class ISensorRepository(ABC):
    @abstractmethod
    def mark_sensor_as_occupied(self, sensor_uuid: uuid.UUID):
        pass

    @abstractmethod
    def get_non_occupied_sensor(self) -> SensorDTO:
        pass
