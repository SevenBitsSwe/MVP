from Models.SensorDAO import SensorDAO
from Models.DatabaseConfig import DatabaseConfig
from abc import ABC, abstractmethod
import uuid



class ISensorRepository(ABC):
    @abstractmethod
    def connect(self, db_config: DatabaseConfig):
        pass

    @abstractmethod
    def mark_sensor_as_occupied(self, sensor_uuid: uuid.UUID):
        pass

    @abstractmethod
    def get_non_occupied_sensor(self) -> SensorDAO:
        pass