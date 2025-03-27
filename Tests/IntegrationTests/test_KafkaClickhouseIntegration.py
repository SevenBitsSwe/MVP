import unittest
from unittest.mock import patch
import uuid
import time
from Models.GeoPosition import GeoPosition
from Models.KafkaConfluentAdapter import KafkaConfluentAdapter
from Models.KafkaConfigParameters import KafkaConfigParameters
from confluent_kafka import Producer
from Models.PositionSender import PositionSender
from Models.PositionJsonAdapter import PositionJsonAdapter
from Models.DatabaseConfigParameters import DatabaseConfigParameters
from Models.DatabaseConnection import DatabaseConnection
import clickhouse_connect

class TestKafkaIntegration(unittest.TestCase):
    
    def setUp(self):
        # Configura componenti reali invece di mock
        self.test_sensor_id = str(uuid.uuid4())
        self.test_position = GeoPosition(
            self.test_sensor_id, 
            45.4642, 
            9.1900, 
            "2025-03-17 14:45:30"
        )
        db_connection = DatabaseConnection(DatabaseConfigParameters())
        self.clickhouse_client = db_connection.connect()
    
    @patch('confluent_kafka.Producer')
    def test_position_sent_to_kafka_are_correctly_stored(self, mock_producer):
        # Test che verifica che una posizione inviata a Kafka generi un messaggio elaborato
        
        # Configura Kafka e invia un messaggio
        config = KafkaConfigParameters()
        config.source_topic = "TestTopic"
        kafka_confluent_adapter : PositionSender = KafkaConfluentAdapter(
                                                config,
                                                PositionJsonAdapter(),
                                                Producer({'bootstrap.servers': KafkaConfigParameters().bootstrap_servers})
                                                )
        kafka_confluent_adapter.send_position(self.test_position)
        time.sleep(10)  # Attendi 10 secondi
        
        # Esegui una query a Clickhouse per verificare che il dato sia stato salvato
        query = f"""
        SELECT user_uuid, latitude, longitude, received_at
        FROM nearyou.test_kafka
        WHERE user_uuid = '{self.test_sensor_id}'
        ORDER BY received_at DESC
        LIMIT 1"""
        result = self.clickhouse_client.query(query)
        self.assertTrue(result.row_count > 0, "Nessun dato trovato in Clickhouse per la posizione inviata")
        # Estrai la riga di risultato
        row = result.first_row
        # Verifica che i dati corrispondano a quelli inviati
        print(f"Dati trovati in Clickhouse: {row}")
        # Verifica l'ID del sensore
        self.assertEqual(str(row[0]), str(self.test_sensor_id), "UUID sensore diverso da quello inviato")
    
       