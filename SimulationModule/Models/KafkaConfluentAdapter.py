from KafkaConfigParameters import KafkaConfigParameters
from KafkaPositionObserver import KafkaPositionObserver
from confluent_kafka import Producer

class KafkaConfluentAdapter(KafkaPositionObserver):
    '''This class implements the KafkaPositionObserver and is used to send the position to a Kafka topic'''
    
    def __init__(self, kafka_config: KafkaConfigParameters):
        '''constructor to initialize the KafkaConfluentAdapter'''
        super().__init__()
        self.__kafka_config = kafka_config
        self.__producer = Producer({'bootstrap.servers': self.__kafka_config.bootstrap_servers})
        
    def _send_data_with_kafka(self):
        '''method to send the data to the Kafka topic'''
        self.__producer.produce(self.__kafka_config.source_topic, 
                                self.__position_serializator.get_json_position().encode('utf-8'))
        self.__producer.flush()
        
    def __del__(self):
        '''destructor to close the producer'''
        self.__producer.flush()
        self.__producer.close()