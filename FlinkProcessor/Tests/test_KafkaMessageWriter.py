import unittest
from unittest.mock import Mock, patch, MagicMock
from Core.KafkaMessageWriter import KafkaMessageWriter
from Core.KafkaWriterConfiguration import KafkaWriterConfiguration
from Core.JsonRowSerializationAdapter import JsonRowSerializationAdapter
from pyflink.datastream.connectors.kafka import KafkaSink, KafkaRecordSerializationSchema
from pyflink.datastream.formats.json import JsonRowSerializationSchema

class TestKafkaMessageWriter(unittest.TestCase):
    
    @patch('Core.KafkaMessageWriter.KafkaRecordSerializationSchema')
    @patch('Core.KafkaMessageWriter.KafkaSink')
    @patch('Core.KafkaMessageWriter.JsonRowSerializationSchema')
    def test_initialization(self, mock_json_schema, mock_kafka_sink, mock_record_schema):
        """verify class initialization"""
        # Configure the mocks
        mock_config = Mock(spec=KafkaWriterConfiguration)
        mock_config.writable_topic = "test-topic"
        mock_config.bootstrap_servers = "localhost:9092"
        mock_config.key_type = "key_type_info"
        
        mock_adapter = Mock(spec=JsonRowSerializationAdapter)
        mock_serialization_schema = Mock()
        mock_adapter.get_serialization_schema.return_value = mock_serialization_schema
        
        # Set up mock builders
        mock_record_schema_builder = Mock()
        mock_record_schema.builder.return_value = mock_record_schema_builder
        mock_record_schema_builder.set_topic.return_value = mock_record_schema_builder
        mock_record_schema_builder.set_key_serialization_schema.return_value = mock_record_schema_builder
        mock_record_schema_builder.set_value_serialization_schema.return_value = mock_record_schema_builder
        mock_record_schema_builder.build.return_value = Mock(name="record_serializer_instance")
        
        mock_json_schema_builder = Mock()
        mock_json_schema.builder.return_value = mock_json_schema_builder
        mock_json_schema_builder.with_type_info.return_value = mock_json_schema_builder
        mock_json_schema_builder.build.return_value = Mock(name="json_schema_instance")
        
        mock_sink_builder = Mock()
        mock_kafka_sink.builder.return_value = mock_sink_builder
        mock_sink_builder.set_bootstrap_servers.return_value = mock_sink_builder
        mock_sink_builder.set_record_serializer.return_value = mock_sink_builder
        mock_sink_builder.build.return_value = Mock(name="kafka_sink_instance")

        # create istance to test
        writer = KafkaMessageWriter(mock_config, mock_adapter)
        
        # verify that all methods have been called with the correct parameters
        mock_record_schema.builder.assert_called_once()
        mock_record_schema_builder.set_topic.assert_called_once_with(mock_config.writable_topic)
        mock_json_schema.builder.assert_called_once()
        mock_json_schema_builder.with_type_info.assert_called_once_with(mock_config.key_type)
        mock_kafka_sink.builder.assert_called_once()
        mock_sink_builder.set_bootstrap_servers.assert_called_once_with(mock_config.bootstrap_servers)
    
    def test_get_message_writer(self):
        """test get_message_writer method"""
        # configure the mock objects
        mock_config = Mock(spec=KafkaWriterConfiguration)
        mock_adapter = Mock(spec=JsonRowSerializationAdapter)
        mock_adapter.get_serialization_schema.return_value = Mock()
        
        # create sink mock
        mock_sink = Mock(name="kafka_sink_mock")
        
        # substitute the build_record_serializer and build_kafka_sink methods with the mock_sink
        with patch.object(KafkaMessageWriter, 'build_record_serializer') as mock_build_record:
            with patch.object(KafkaMessageWriter, 'build_kafka_sink') as mock_build_sink:
                mock_build_sink.return_value = mock_sink
                
                #create the instance to test
                writer = KafkaMessageWriter(mock_config, mock_adapter)
                
                # Verify that the method returns the correct object
                self.assertEqual(writer.get_message_writer(), mock_sink)
