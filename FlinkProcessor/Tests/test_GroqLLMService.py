import unittest
from unittest.mock import patch, MagicMock
import os
from Core.GroqLLMService import GroqLLMService
from Core.StructuredResponseMessage import StructuredResponseMessage

class TestGroqLLMService(unittest.TestCase):
    """Test suite for the GroqLLMService class."""

    @patch.dict(os.environ, {"PYTHON_PROGRAM_KEY": "test-api-key"})
    def setUp(self):
        """Set up the test environment."""
        self.structured_response = StructuredResponseMessage
        self.service = GroqLLMService(self.structured_response)

    @patch.dict(os.environ, {"PYTHON_PROGRAM_KEY": "test-api-key"})
    def test_initialization(self):
        """Test that GroqLLMService initializes correctly."""
        service = GroqLLMService(self.structured_response)

        # Verify the API key was loaded from environment
        self.assertEqual(service._GroqLLMService__groq_api_key, "test-api-key")

        # Verify structured_response is stored
        self.assertEqual(service._llm_structured_response, self.structured_response)

        # Verify chat is initially None
        self.assertIsNone(service._GroqLLMService__chat)

    @patch('Core.GroqLLMService.InMemoryRateLimiter')
    @patch('Core.GroqLLMService.ChatGroq')
    @patch.dict(os.environ, {"PYTHON_PROGRAM_KEY": "test-api-key"})
    def test_set_up_chat(self, mock_chat_groq, mock_rate_limiter):
        """Test that set_up_chat configures ChatGroq correctly."""
        # Configure mocks
        mock_rate_limiter_instance = MagicMock()
        mock_rate_limiter.return_value = mock_rate_limiter_instance

        mock_chat_instance = MagicMock()
        mock_chat_groq.return_value = mock_chat_instance

        # Call the method to test
        self.service.set_up_chat()

        # Verify rate limiter is created with correct parameters
        mock_rate_limiter.assert_called_once_with(
            requests_per_second=0.065,
            check_every_n_seconds=0.1,
            max_bucket_size=10
        )

        # Verify ChatGroq is created with correct parameters
        mock_chat_groq.assert_called_once_with(
            groq_api_key="test-api-key",
            model="Gemma2-9b-it",
            temperature=0.6,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            cache=False,
            rate_limiter=mock_rate_limiter_instance
        )

        # Verify chat is stored
        self.assertEqual(self.service._GroqLLMService__chat, mock_chat_instance)

    @patch.dict(os.environ, {"PYTHON_PROGRAM_KEY": "test-api-key"})
    def test_get_llm_structured_response(self):
        """Test that get_llm_structured_response calls the model correctly."""
        # Create mock chat instance
        mock_chat = MagicMock()
        self.service._GroqLLMService__chat = mock_chat

        # Create mock structured_model
        mock_structured_model = MagicMock()
        mock_chat.with_structured_output.return_value = mock_structured_model

        # Create expected response using StructuredResponseMessage
        expected_response = StructuredResponseMessage(
            pubblicita="Scopri la nuova palestra FitLife, il posto ideale per raggiungere i tuoi obiettivi di fitness. Con attrezzature all'avanguardia, trainer qualificati e un ambiente accogliente, ti aiuteremo a migliorare il tuo benessere fisico. Approfitta della nostra offerta di prova gratuita e inizia oggi stesso il tuo percorso verso una vita più sana e attiva!",
            attivita="FitLife Gym"
        )
        mock_structured_model.invoke.return_value = expected_response

        # Call the method to test
        test_prompt = "Crea una pubblicità per una palestra rivolta a un giovane professionista"
        result = self.service.get_llm_structured_response(test_prompt)

        # Verify with_structured_output is called with correct parameters
        mock_chat.with_structured_output.assert_called_once_with(self.structured_response)

        # Verify invoke is called with correct prompt
        mock_structured_model.invoke.assert_called_once_with(test_prompt)

        # Verify response is returned correctly
        self.assertEqual(result, expected_response)
        self.assertEqual(result.pubblicita, expected_response.pubblicita)
        self.assertEqual(result.attivita, "FitLife Gym")