import unittest
from unittest.mock import Mock
from datetime import datetime
from Core.MessageSerializer import MessageSerializer
from Core.MessageDTO import MessageDTO
from pyflink.common.types import Row

class TestMessageSerializer(unittest.TestCase):
    
    def setUp(self):
        """Setup per i test con un MessageDTO di esempio"""
        # Crea un oggetto MessageDTO di esempio
        self.sample_message = MessageDTO(
            user_id="user123",
            activity_id="activity456",
            message_id="message789",
            message_text="Test message content",
            activity_lat=45.4642,
            activity_lon=9.1900,
            creation_time=datetime(2025, 3, 17, 14, 30, 0),
            user_lat=45.4646,
            user_lon=9.1904
        )
        
        # Istanza del serializzatore da testare
        self.serializer = MessageSerializer()
    
    def test_create_row_from_message(self):
        """Verifica che il metodo create_row_from_message crei correttamente un oggetto Row"""
        # Chiama il metodo da testare
        result = self.serializer.create_row_from_message(self.sample_message)
        
        # Verifica che il risultato sia un oggetto Row
        self.assertIsInstance(result, Row)
        
        # Verifica che i valori nel Row siano quelli attesi
        self.assertEqual(result[0], "user123")
        self.assertEqual(result[1], "activity456")
        self.assertEqual(result[2], "message789")
        self.assertEqual(result[3], "Test message content")
        self.assertEqual(result[4], 45.4642)
        self.assertEqual(result[5], 9.1900)
        self.assertEqual(result[6], str(self.sample_message.creation_time))
        self.assertEqual(result[7], 45.4646)
        self.assertEqual(result[8], 9.1904)
        
        # Verifica che l'oggetto Row contenga il numero corretto di elementi
        self.assertEqual(len(result), 9)