import unittest
from Models.KafkaConfigParameters import KafkaConfigParameters

class TestKafkaConfigParameters(unittest.TestCase):
    """Test case per la classe KafkaConfigParameters"""

    def test_default_values(self):
        """Verifica che l'istanza venga creata con i valori predefiniti corretti"""
        config = KafkaConfigParameters()
        self.assertEqual("kafka:9092", config.bootstrap_servers)
        self.assertEqual("SimulatorPosition", config.source_topic)