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

        activity_info = {
            "name": "Concerto nel Parco",
            "type": "Music",
            "description": "Un concerto all'aperto con artisti locali",
            "address": "Parco Centrale, Milano"
        }

        # Generate the prompt
        result = self.custom_prompt.get_prompt(user_info, activity_info)

        # Verify the result contains the expected elements
        self.assertIsInstance(result, str)
        self.assertIn("John Doe", result)
        self.assertIn("Concerto nel Parco", result)
        self.assertIn("Music", result)
        self.assertIn("Parco Centrale", result)

        # General checks on the content without searching for exact sentences
        self.assertTrue(len(result) > 0)

    def test_get_prompt_empty_data(self):
        """Test handling of empty data."""
        # Empty user info and activities
        user_info = {}
        activity_info = {}

        # Generate the prompt with empty data
        result = self.custom_prompt.get_prompt(user_info, activity_info)

        # Verify the result still contains the template structure
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

        # Verify that the output has a correct structure even with empty data
        self.assertNotIn(" - ", result)
