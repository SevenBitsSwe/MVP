import unittest
from unittest.mock import MagicMock

from Core.FilterMessageAlreadyDisplayed import FilterMessageAlreadyDisplayed
from Core.IMessageRepository import IMessageRepository
from Core.MessageDTO import MessageDTO

class TestFilterMessageAlreadyDisplayed(unittest.TestCase):
    def setUp(self):
        # mock message repository , necessary for filter constructor
        self.message_repository = MagicMock(spec=IMessageRepository)

        # create the filter instance to use in the tests
        self.filter = FilterMessageAlreadyDisplayed(self.message_repository)

    def test_open(self):
        """test open method which does practically nothing"""
        runtime_context = MagicMock()

        # Execute the method to test
        self.filter.open(runtime_context)

    def test_filter_same_coordinates(self):
        """Case test , wehre the message has the very same coordinates as the last message (should be filtered)"""
        # Mock input data
        user_id = "10000000-0000-0000-0000-000000000000"
        activity_id = "act123"
        message_id = "msg123"
        message_text = "Visita questo luogo!"
        activity_lat = 45.4642
        activity_lon = 9.1900
        timestamp = "2025-03-17 14:45:30"
        user_lat = 45.4650
        user_lon = 9.1910

        # Create ROW input
        input_value = [user_id, activity_id, message_id, message_text,
                       activity_lat, activity_lon, timestamp, user_lat, user_lon]

        # Mock messageDTO with same coordinates
        last_message = MagicMock(spec=MessageDTO)
        last_message.activity_lat = 45.4642
        last_message.activity_lon = 9.1900
        self.message_repository.get_user_last_message.return_value = last_message

        # Execute filter method
        result = self.filter.filter(input_value)

        # Verify that the message has been filtered
        self.message_repository.get_user_last_message.assert_called_once_with(user_id)
        self.assertFalse(result)

    def test_filter_different_coordinates(self):
        """Case test where the message has different coordinates from the last message (should not be filtered)"""
        # Mock input data
        user_id = "10000000-0000-0000-0000-000000000000"
        activity_id = "act123"
        message_id = "msg123"
        message_text = "Visita questo luogo!"
        activity_lat = 45.4642
        activity_lon = 9.1900
        timestamp = "2025-03-17 14:45:30"
        user_lat = 45.4650
        user_lon = 9.1910

        input_value = [user_id, activity_id, message_id, message_text,
                       activity_lat, activity_lon, timestamp, user_lat, user_lon]

        # Mock last message with different coordinates
        last_message = MagicMock(spec=MessageDTO)
        last_message.activity_lat = 45.5000
        last_message.activity_lon = 9.2000
        self.message_repository.get_user_last_message.return_value = last_message

        # execute the filter method
        result = self.filter.filter(input_value)

        # verify that the message has not been filtered, so it will be sent
        self.message_repository.get_user_last_message.assert_called_once_with(user_id)
        self.assertTrue(result)

    def test_filter_zero_coordinates(self):
        """case test where the message has coordinates (0,0) and should be filtered"""
        # Prepare input data
        user_id = "10000000-0000-0000-0000-000000000000"
        activity_id = "act123"
        message_id = "msg123"
        message_text = "skip-this-message"
        activity_lat = 0.0
        activity_lon = 0.0
        timestamp = "2025-03-17 14:45:30"
        user_lat = 45.4650
        user_lon = 9.1910

        input_value = [user_id, activity_id, message_id, message_text,
                       activity_lat, activity_lon, timestamp, user_lat, user_lon]

        # Mock last message , in this case it does not matter the coordinates value
        last_message = MagicMock(spec=MessageDTO)
        last_message.activity_lat = 45.5000
        last_message.activity_lon = 9.2000
        self.message_repository.get_user_last_message.return_value = last_message

        # execute filter method
        result = self.filter.filter(input_value)

        # verify that the message has been filtered
        self.message_repository.get_user_last_message.assert_called_once_with(user_id)
        self.assertFalse(result)

    def test_filter_rounding(self):
        """Case test where the coordinates are the same after rounding to 4 decimals"""
        # Prepare input data
        user_id = "10000000-0000-0000-0000-000000000000"
        activity_id = "act123"
        message_id = "msg123"
        message_text = "Visita questo luogo!"
        activity_lat = 45.46421
        activity_lon = 9.19001
        timestamp = "2025-03-17 14:45:30"
        user_lat = 45.4650
        user_lon = 9.1910

        input_value = [user_id, activity_id, message_id, message_text,
                       activity_lat, activity_lon, timestamp, user_lat, user_lon]

        # Mock last message with coordinates that are the same after rounding
        last_message = MagicMock(spec=MessageDTO)
        last_message.activity_lat = 45.46422
        last_message.activity_lon = 9.19003
        self.message_repository.get_user_last_message.return_value = last_message

        #Execute filter method
        result = self.filter.filter(input_value)

        # VEerify that the message has been filtered, since the coordinates are the same after rounding
        self.message_repository.get_user_last_message.assert_called_once_with(user_id)
        self.assertFalse(result)
