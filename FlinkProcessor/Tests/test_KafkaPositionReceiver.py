import unittest
from unittest.mock import Mock, patch
from Core.KafkaPositionReceiver import KafkaPositionReceiver
from Core.KafkaSourceConfiguration import KafkaSourceConfiguration
from Core.JsonRowDeserializationAdapter import JsonRowDeserializationAdapter
from pyflink.datastream.connectors.kafka import KafkaSource

#TU13
class TestKafkaPositionReceiver(unittest.TestCase):
    
    def setUp(self):
        # Mock configuration
        self.mock_config = Mock(spec=KafkaSourceConfiguration)
        self.mock_config.bootstrap_servers = "localhost:9092"
        self.mock_config.source_topic = "test-topic"
        self.mock_config.group_id = "test-group"
        self.mock_config.enable_auto_commit = "true"
        self.mock_config.commit_offsets_on_checkpoint = "true"
        
        # Mock deserializer
        self.mock_deserializer = Mock(spec=JsonRowDeserializationAdapter)
        self.mock_deserializer.get_deserialization_schema.return_value = Mock()
        
        # mock builder KafkaSource
        self.mock_builder = Mock()
        self.mock_builder.set_bootstrap_servers.return_value = self.mock_builder
        self.mock_builder.set_topics.return_value = self.mock_builder
        self.mock_builder.set_group_id.return_value = self.mock_builder
        self.mock_builder.set_value_only_deserializer.return_value = self.mock_builder
        self.mock_builder.set_property.return_value = self.mock_builder
        self.mock_builder.build.return_value = Mock(spec=KafkaSource)

    @patch('Core.KafkaPositionReceiver.KafkaSource.builder')
    def test_build_kafka_source(self, mock_kafka_builder):
        # configure the mock of KafkaSource.builder() to return our mock_builder
        mock_kafka_builder.return_value = self.mock_builder
        
        # initialize test object
        receiver = KafkaPositionReceiver(self.mock_config, self.mock_deserializer)
        
        # assert is called once
        mock_kafka_builder.assert_called_once()
        
        # verify all methods has been called with the correct parameters
        self.mock_builder.set_bootstrap_servers.assert_called_once_with(self.mock_config.bootstrap_servers)
        self.mock_builder.set_topics.assert_called_once_with(self.mock_config.source_topic)
        self.mock_builder.set_group_id.assert_called_once_with(self.mock_config.group_id)
        self.mock_builder.set_value_only_deserializer.assert_called_once_with(
            self.mock_deserializer.get_deserialization_schema.return_value)
        
        # Verifica che set_property sia stato chiamato due volte con i parametri corretti
        self.mock_builder.set_property.assert_any_call("enable.auto.commit", self.mock_config.enable_auto_commit)
        self.mock_builder.set_property.assert_any_call(
            "commit.offsets.on.checkpoint", self.mock_config.commit_offsets_on_checkpoint)
        
        # lastly verify build method has been called
        self.mock_builder.build.assert_called_once()
    
    @patch('Core.KafkaPositionReceiver.KafkaSource.builder')
    def test_get_position_receiver(self, mock_kafka_builder):
        # configure the mock of KafkaSource.builder() to return our mock_builder
        mock_kafka_builder.return_value = self.mock_builder
        mock_kafka_source = self.mock_builder.build.return_value
        
        # initialize test object
        receiver = KafkaPositionReceiver(self.mock_config, self.mock_deserializer)
        
        # call the method to test
        result = receiver.get_position_receiver()
        
        #verify the result is the expected one
        self.assertEqual(result, mock_kafka_source)

if __name__ == '__main__':
    unittest.main()