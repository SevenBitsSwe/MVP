from Models.KafkaConfigParameters import KafkaConfigParameters
from Models.PositionSender import PositionSender
from confluent_kafka import Producer

class KafkaConfluentAdapter(PositionSender):
    '''This class implements the KafkaPositionObserver and is used to send the position to a Kafka topic'''
    
    def __init__(self,
                kafka_config: KafkaConfigParameters,
                json_adapter_istance: "PositionJsonAdapter",
                producer_istance: Producer):
        '''constructor to initialize the KafkaConfluentAdapter'''
        super().__init__(json_adapter_istance)
        self.__kafka_config = kafka_config
        self.__producer = producer_istance
        
    def send_data_to_broker(self, json_payload, sensor_id: str):
        '''method to send the data to the Kafka topic'''
        self.__producer.produce(self.__kafka_config.source_topic, 
                                key = str(sensor_id),
                                value = json_payload.encode('utf-8'))
        self.__producer.flush()
        
