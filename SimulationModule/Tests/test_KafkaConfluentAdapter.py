from Models.KafkaConfigParameters import KafkaConfigParameters
from Models.KafkaPositionObserver import KafkaPositionObserver
from Models.KafkaConfluentAdapter import KafkaConfluentAdapter
from Models.PositionJsonAdapter import PositionJsonAdapter
from Models.GpsSensor import GpsSensor
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
    

    def test_on_sensor_data_changed(self):
        """Testa che on_sensor_data_changed chiami correttamente send_data_with_kafka"""
        # Arrange
        sensor_uuid = uuid.uuid4()
        mock_position = MagicMock(spec=GeoPosition)
        serialized_json = '{"data": "serialized"}'
        
        mock_sensor = MagicMock(spec=GpsSensor)
        mock_sensor.get_current_data.return_value = mock_position
        mock_sensor.get_sensor_uuid.return_value = sensor_uuid
        
        self.mock_json_adapter.serialize_to_json.return_value = serialized_json
        
        self.adapter.on_sensor_data_changed(mock_sensor)
        
        mock_sensor.get_current_data.assert_called_once()
        mock_sensor.get_sensor_uuid.assert_called_once()
        
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
            mock_sensor = MagicMock(spec=GpsSensor)
            mock_position = MagicMock(spec=GeoPosition)
            mock_sensor.get_current_data.return_value = mock_position
            
            # call the method that should use lock
            adapter.on_sensor_data_changed(mock_sensor)
            
            # verify lock acquire and release
            mock_lock.__enter__.assert_called_once()
            mock_lock.__exit__.assert_called_once()
        