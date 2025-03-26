import unittest
from unittest.mock import Mock
from datetime import datetime
from Core.MessageSerializer import MessageSerializer
from Core.MessageDTO import MessageDTO
from pyflink.common.types import Row

#TU16
class TestMessageSerializer(unittest.TestCase):
    
    def setUp(self):
        """Setup for tests with a sample MessageDTO"""
        # Create a sample MessageDTO object
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
        
        # Instance of the serializer to be tested
        self.serializer = MessageSerializer()
    
    def test_create_row_from_message(self):
        """Verify that the create_row_from_message method correctly creates a Row object"""
        # Call the method to be tested
        result = self.serializer.create_row_from_message(self.sample_message)
        
        # Verify that the result is a Row object
        self.assertIsInstance(result, Row)
        
        # Verify that the values in the Row are the expected ones
        self.assertEqual(result[0], "user123")
        self.assertEqual(result[1], "activity456")
        self.assertEqual(result[2], "message789")
        self.assertEqual(result[3], "Test message content")
        self.assertEqual(result[4], 45.4642)
        self.assertEqual(result[5], 9.1900)
        self.assertEqual(result[6], str(self.sample_message.creation_time))
        self.assertEqual(result[7], 45.4646)
        self.assertEqual(result[8], 9.1904)
        
        # Verify that the Row object contains the correct number of elements
        self.assertEqual(len(result), 9)