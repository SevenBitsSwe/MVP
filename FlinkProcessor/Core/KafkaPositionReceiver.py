from pyflink.datastream.connectors.kafka import KafkaSource
from Core.IPositionReceiver import IPositionReceiver
from Core.KafkaSourceConfiguration import KafkaSourceConfiguration
from Core.JsonRowDeserializationAdapter import JsonRowDeserializationAdapter

class KafkaPositionReceiver(IPositionReceiver):
    '''Adapter for receiving positions from Kafka'''
    def __init__(self, kafka_source_configuration: KafkaSourceConfiguration,
                  deserialize_adapter: JsonRowDeserializationAdapter):
        self.__current_configuration = kafka_source_configuration
        self.__position_deserializer = deserialize_adapter.get_deserialization_schema()
        self.__kafka_source = self.build_kafka_source()

    def build_kafka_source(self) -> KafkaSource:
        return KafkaSource.builder() \
                            .set_bootstrap_servers(self.__current_configuration.bootstrap_servers) \
                            .set_topics(self.__current_configuration.source_topic) \
                            .set_group_id(self.__current_configuration.group_id) \
                            .set_value_only_deserializer(self.__position_deserializer) \
                            .set_property("enable.auto.commit", self.__current_configuration.enable_auto_commit) \
                            .set_property("commit.offsets.on.checkpoint", self.__current_configuration.commit_offsets_on_checkpoint) \
                            .build()

    def get_position_receiver(self):
        '''interface implementation'''
        return self.__kafka_source
