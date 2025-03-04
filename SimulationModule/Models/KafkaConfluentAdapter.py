from Models.KafkaConfigParameters import KafkaConfigParameters
from Models.KafkaPositionObserver import KafkaPositionObserver
from confluent_kafka import Producer

class KafkaConfluentAdapter(KafkaPositionObserver):
    '''This class implements the KafkaPositionObserver and is used to send the position to a Kafka topic'''
    
    def __init__(self, kafka_config: KafkaConfigParameters):
        '''constructor to initialize the KafkaConfluentAdapter'''
        super().__init__()
        self.__kafka_config = kafka_config
        self.__producer = Producer({'bootstrap.servers': self.__kafka_config.bootstrap_servers})
        
    def send_data_with_kafka(self, json_payload):
        '''method to send the data to the Kafka topic'''
        self.__producer.produce(self.__kafka_config.source_topic, 
                                json_payload.encode('utf-8'))
        self.__producer.flush()
        