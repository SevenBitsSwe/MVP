from Models.KafkaConfigParameters import KafkaConfigParameters
from Models.KafkaPositionObserver import KafkaPositionObserver
from Models.KafkaConfluentAdapter import KafkaConfluentAdapter
from Models.PositionJsonAdapter import PositionJsonAdapter
import unittest
from confluent_kafka import Producer

from unittest.mock import MagicMock,patch


class TestKafkaConfluentAdapter(unittest.TestCase):

    def setUp(self):
        self.kafka_config = KafkaConfigParameters()
        self.mock_json_adapter = MagicMock(spec=PositionJsonAdapter)
        self.mock_producer = MagicMock( spec = Producer)
        
        self.adapter = KafkaConfluentAdapter(
            self.kafka_config, 
            self.mock_json_adapter,
            self.mock_producer
        )
    
    def test_send_data_with_kafka(self):
        # Arrange
        json_payload = '{"id": "test_id", "latitude": 0.0, "longitude": 0.0, "received_at": "2025-03-05 14:30:00"}'
        sensor_key = "test_id"
        
        # Act
        self.adapter.send_data_with_kafka(json_payload, sensor_key)
        
        # Assert
        self.mock_producer.produce.assert_called_once_with(
            self.kafka_config.source_topic,
            key=str(sensor_key),
            value=json_payload.encode('utf-8')
        )
        
        self.mock_producer.flush.assert_called_once()