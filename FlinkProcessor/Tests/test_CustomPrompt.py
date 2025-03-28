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

        # Verifica più generica sul contenuto senza cercare frasi esatte
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

        # Verifica che l'output abbia una struttura corretta anche con dati vuoti
        self.assertNotIn(" - ", result)  # No activity items should be present
