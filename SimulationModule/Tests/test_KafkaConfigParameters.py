import unittest
from Models.KafkaConfigParameters import KafkaConfigParameters

class TestKafkaConfigParameters(unittest.TestCase):

    def test_default_values(self):
        config = KafkaConfigParameters()
        self.assertEqual("kafka:9092", config.bootstrap_servers)
        self.assertEqual("SimulatorPosition", config.source_topic)
