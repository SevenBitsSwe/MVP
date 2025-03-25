from pyflink.datastream.connectors.kafka import KafkaSink,KafkaRecordSerializationSchema
from pyflink.datastream.formats.json import JsonRowSerializationSchema
from Core.IMessageWriter import IMessageWriter
from Core.JsonRowSerializationAdapter import JsonRowSerializationAdapter
from Core.KafkaWriterConfiguration import KafkaWriterConfiguration

class KafkaMessageWriter(IMessageWriter):
    '''Adapter for writing messages to Kafka'''
    def __init__(self, kafka_writer_configuration: KafkaWriterConfiguration,
                  serialize_adapter: JsonRowSerializationAdapter):
        self.__current_configuration = kafka_writer_configuration
        self.__position_serializer = serialize_adapter.get_serialization_schema()
        self.__record_serializer = self.build_record_serializer()
        self.__kafka_sink = self.build_kafka_sink()

    def build_record_serializer(self):
        return KafkaRecordSerializationSchema.builder() \
                                            .set_topic(self.__current_configuration.writable_topic) \
                                            .set_key_serialization_schema(JsonRowSerializationSchema.builder()\
                                                        .with_type_info(self.__current_configuration.key_type)\
                                                        .build())\
                                            .set_value_serialization_schema(self.__position_serializer) \
                                            .build()

    def build_kafka_sink(self):
        return KafkaSink.builder() \
                        .set_bootstrap_servers(self.__current_configuration.bootstrap_servers) \
                        .set_record_serializer(self.__record_serializer) \
                        .build()

    def get_message_writer(self):
        '''interface implementation'''
        return self.__kafka_sink
