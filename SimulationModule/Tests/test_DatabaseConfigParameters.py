import unittest
from Models.DatabaseConfigParameters import DatabaseConfigParameters

# TU19
class TestKafkaConfigParameters(unittest.TestCase):

    def test_default_values(self):
        config = DatabaseConfigParameters()
        self.assertEqual("clickhouse", config.host)
        self.assertEqual("8123", config.port)
        self.assertEqual("default", config.user)
        self.assertEqual("pass", config.password)
