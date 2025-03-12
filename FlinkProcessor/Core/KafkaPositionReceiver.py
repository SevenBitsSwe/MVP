from Core.IPositionReceiver import IpositionReceiver
from pyflink.datastream.connectors.kafka import KafkaSource
from Core.KafkaSourceConfiguration import KafkaSourceConfiguration
from Core.JsonRowDeserializationAdapter import JsonRowDeserializationAdapter

class KafkaPositionReceiver(IpositionReceiver):
    '''Adapter for receiving positions from Kafka'''
    def __init__(self, kafka_source_configuration: KafkaSourceConfiguration,
                  deserialize_adapter: JsonRowDeserializationAdapter):
        self.__current_configuration = kafka_source_configuration
        self.__position_deserializer = deserialize_adapter
        self.__kafka_source = self.build_kafka_source()
       

    def build_kafka_source(self) -> KafkaSource:
        
        return KafkaSource.builder() \
                            .set_bootstrap_servers(self.__current_configuration.bootstrap_servers) \
                            .set_topics(self.__current_configuration.topic) \
                            .set_group_id(self.__current_configuration.group_id) \
                            .set_value_only_deserializer(self.__position_deserializer) \
                            .set_property("enable.auto.commit", self.__current_configuration.enable_auto_commit) \
                            .set_property("commit.offsets.on.checkpoint", self.__current_configuration.commit_offsets_on_checkpoint) \
                            .build()

    