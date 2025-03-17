import unittest
from ..Core.KafkaSourceConfiguration import KafkaSourceConfiguration

class TestKafkaSourceConfiguration(unittest.TestCase):
    
    def test_default_initialization(self):
        """Test initialization with default values"""
        config = KafkaSourceConfiguration()
        
        self.assertEqual(config.bootstrap_servers, "kafka:9092")
        self.assertEqual(config.source_topic, "SimulatorPosition")
        self.assertEqual(config.group_id, "pyfinkJob")
        self.assertEqual(config.enable_auto_commit, "true")
        self.assertEqual(config.commit_offsets_on_checkpoint, "true")