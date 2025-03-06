from Models.IPositionObserver import IPositionObserver
from Models.GpsSensor import GpsSensor
from Models.IJsonSerializable import IJsonSerializable
import threading
from abc import ABC, abstractmethod

class KafkaPositionObserver(IPositionObserver,ABC):
    '''This class implements the observer interface and is used to observe the GPS sensor position and
    write the position to a Kafka topic, note this class will be inherited by a KafkaConfluentAdapter'''
    
    def __init__(self, json_adapter_istance: IJsonSerializable):
        '''constructor to initialize the kafka position observer'''
        self.__position_serializator = json_adapter_istance
        self._lock = threading.Lock()

    @abstractmethod
    def send_data_with_kafka(self, json_payload, sensor_key: str):
        '''abstract method to send the data to the Kafka topic'''
        pass

    def on_sensor_data_changed(self, sensor_istance: GpsSensor):
        '''function call to send data will automatically be called in the subclass implementation'''
        with self._lock:
            self.send_data_with_kafka(
                self.__position_serializator.serialize_to_json(sensor_istance.get_current_data()),
                sensor_istance.get_sensor_uuid()
            )
        