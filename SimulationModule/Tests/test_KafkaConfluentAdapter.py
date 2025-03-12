from Models.KafkaConfigParameters import KafkaConfigParameters
from Models.KafkaConfluentAdapter import KafkaConfluentAdapter
from Models.PositionJsonAdapter import PositionJsonAdapter
from Models.GeoPosition import GeoPosition
import unittest
import uuid
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
        sensor_id = "test_id"
        
        # Act
        self.adapter.send_data_to_broker(json_payload, sensor_id)
        
        # Assert
        self.mock_producer.produce.assert_called_once_with(
            self.kafka_config.source_topic,
            key=str(sensor_id),
            value=json_payload.encode('utf-8')
        )
        
        self.mock_producer.flush.assert_called_once()
    

    def test_send_position(self):
        """Testa che on_sensor_data_changed chiami correttamente send_data_with_kafka"""
        # Arrange
        sensor_uuid = uuid.uuid4()
        mock_position = MagicMock(spec=GeoPosition)
        serialized_json = '{"data": "serialized"}'
        
        self.mock_json_adapter.serialize_to_json.return_value = serialized_json
        
        self.adapter.send_position(mock_position)
        
        mock_position.get_sensor_id.assert_called_once()
        
        self.mock_json_adapter.serialize_to_json.assert_called_once_with(mock_position)
        
        self.mock_producer.produce.assert_called_once_with(
            self.kafka_config.source_topic,
            key=str(sensor_uuid),
            value=serialized_json.encode('utf-8')
        )

    def test_thread_safety(self):
    
        with patch('threading.Lock') as mock_lock_class:
            mock_lock = MagicMock()
            mock_lock_class.return_value = mock_lock
            
            # create an istance of the adapter
            adapter = KafkaConfluentAdapter(self.kafka_config, self.mock_json_adapter, self.mock_producer)
            
            # configure mock sensor
            mock_position = MagicMock(spec=GeoPosition)
           
            # call the method that should use lock
            adapter.send_position(mock_position)
            
            # verify lock acquire and release
            mock_lock.__enter__.assert_called_once()
            mock_lock.__exit__.assert_called_once()
        
