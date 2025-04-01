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

    def test_filter_new_message_should_pass(self):
        """Test that verifies that a message for an activity not yet shown to the user passes the filter"""
        # Arrange
        # Mock input data
        user_id = "10000000-0000-0000-0000-000000000000"
        activity_id = "30000000-0000-0000-0000-000000000000"
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
        
        # Configuring a mock to simulate an activity not yet shown
        self.message_repository.check_activity_already_displayed_for_user.return_value = False
                
        # Act
        result = self.filter.filter(input_value)
        
        # Assert
        self.assertTrue(result)
        self.message_repository.check_activity_already_displayed_for_user.assert_called_once_with(user_id, activity_id)
    
    def test_filter_already_displayed_message_should_not_pass(self):
        """Test that verifies that a message for an activity already shown to the user is filtered"""
        # Arrange
        user_id = "10000000-0000-0000-0000-000000000000"
        activity_id = "30000000-0000-0000-0000-000000000000"
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
        
        # Configuring a mock to simulate an already displayed activity
        self.message_repository.check_activity_already_displayed_for_user.return_value = True
        # Act
        result = self.filter.filter(input_value)
        # Assert
        self.assertFalse(result)
        self.message_repository.check_activity_already_displayed_for_user.assert_called_once_with(user_id, activity_id)
    
    def test_filter_zero_coordinates_should_not_pass(self):
        """Test that verifies that a message with coordinates (0,0) is always filtered"""
        # Arrange
        user_id = "10000000-0000-0000-0000-000000000000"
        activity_id = "30000000-0000-0000-0000-000000000000"
        message_id = "msg123"
        message_text = "Visita questo luogo!"
        activity_lat = 0.0
        activity_lon = 0.0
        timestamp = "2025-03-17 14:45:30"
        user_lat = 45.4650
        user_lon = 9.1910

        # Create ROW input
        input_value = [user_id, activity_id, message_id, message_text,
                       activity_lat, activity_lon, timestamp, user_lat, user_lon]
        
        self.message_repository.check_activity_already_displayed_for_user.return_value = False
        
        # Preparing input data with coordinates (0,0)
        
        # Act
        result = self.filter.filter(input_value)
        
        # Assert
        self.assertFalse(result)
        # Check that the repository was called anyway
        self.message_repository.check_activity_already_displayed_for_user.assert_called_once_with(user_id, activity_id)
