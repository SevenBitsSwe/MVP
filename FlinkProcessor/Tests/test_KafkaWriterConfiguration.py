import unittest
from pyflink.common import Types
from pyflink.common.typeinfo import TypeInformation
from Core.KafkaWriterConfiguration import KafkaWriterConfiguration

class TestKafkaWriterConfiguration(unittest.TestCase):    
    def test_default_values(self):
        """Test default configuration values"""
        config = KafkaWriterConfiguration()
        
        # verify default values
        self.assertEqual(config.bootstrap_servers, "kafka:9092")
        self.assertEqual(config.writable_topic, "MessageElaborated")
        
        # Verify key_type and row_type_info_message are TypeInformation
        self.assertIsInstance(config.key_type, TypeInformation)
        self.assertIsInstance(config.row_type_info_message, TypeInformation)
        
    
    def test_key_type_structure(self):
        """test key_type structure"""
        config = KafkaWriterConfiguration()
        
        # Define the expected structure of the key_type
        reference_key_type = Types.ROW_NAMED(
            ['user_uuid'],
            [Types.STRING()]
        )
        
        # verify key type structure is correct
        self.assertEqual(str(config.key_type), str(reference_key_type))