from abc import ABC, abstractmethod
import uuid
from Models.SensorDAO import SensorDAO


class ISensorRepository(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def mark_sensor_as_occupied(self, sensor_uuid: uuid.UUID):
        pass

    @abstractmethod
    def get_non_occupied_sensor(self) -> SensorDAO:
        pass