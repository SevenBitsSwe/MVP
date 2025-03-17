import unittest
from Core.CustomPrompt import CustomPrompt

class TestCustomPrompt(unittest.TestCase):
    """Test suite for the CustomPrompt class."""

    def setUp(self):
        """Set up the test environment."""
        self.custom_prompt = CustomPrompt()
        
    def test_get_prompt_formatting(self):
        """Test that get_prompt correctly formats the template with provided data."""
        # Sample data for testing
        user_info = {
            "name": "John Doe",
            "age": 30,
            "interests": ["Sport", "Music", "Technology"]
        }
        
        activities = {
            "Concert in the Park": {"type": "Music", "lat": 45.4642, "lon": 9.1900},
            "Tech Workshop": {"type": "Technology", "lat": 45.4867, "lon": 9.1821},
            "Football Match": {"type": "Sport", "lat": 45.4785, "lon": 9.1236}
        }
        
        # Generate the prompt
        result = self.custom_prompt.get_prompt(user_info, activities)
        
        # Verify the result contains the expected elements
        self.assertIsInstance(result, str)
        self.assertIn("John Doe", result)
        self.assertIn("Concert in the Park", result)
        self.assertIn("Tech Workshop", result)
        self.assertIn("Football Match", result)
        
        # Verifica più generica sul contenuto senza cercare frasi esatte
        self.assertTrue(len(result) > 0)
        self.assertTrue(any(activity in result for activity in activities.keys()))
        
    def test_get_prompt_empty_data(self):
        """Test handling of empty data."""
        # Empty user info and activities
        user_info = {}
        activities = {}
        
        # Generate the prompt with empty data
        result = self.custom_prompt.get_prompt(user_info, activities)
        
        # Verify the result still contains the template structure
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        
        # Verifica che l'output abbia una struttura corretta anche con dati vuoti
        self.assertNotIn(" - ", result)  # No activity items should be present