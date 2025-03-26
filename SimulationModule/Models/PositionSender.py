import threading
from abc import ABC, abstractmethod
from Models.GeoPosition import GeoPosition
from Models.IJsonSerializable import IJsonSerializable

class PositionSender(ABC):
    '''This class implements the observer interface and is used to observe the GPS sensor position and
    write the position to a Kafka topic, note this class will be inherited by a KafkaConfluentAdapter'''

    def __init__(self, json_adapter_istance: IJsonSerializable):
        '''constructor to initialize the kafka position observer'''
        self.__position_serializator = json_adapter_istance
        self._lock = threading.Lock()

    @abstractmethod
    def send_data_to_broker(self, json_payload, sensor_id: str):
        '''abstract method to send the data to the Kafka topic'''
        pass

    def send_position(self, position: GeoPosition):
        '''function call to send data will automatically be called in the subclass implementation'''
        with self._lock:
            self.send_data_to_broker(
                self.__position_serializator.serialize_to_json(position),
                position.get_sensor_id()
            )
