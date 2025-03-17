import unittest
from unittest.mock import Mock, patch, MagicMock

from pyflink.common import Types
from pyflink.datastream.formats.json import JsonRowDeserializationSchema
from Core.JsonRowDeserializationAdapter import JsonRowDeserializationAdapter

class TestJsonRowDeserializationAdapter(unittest.TestCase):
    
    def setUp(self):
        # Create type info as position schema
        self.sample_type_info = Types.ROW_NAMED(
            ['user_uuid', 'latitude','longitude', 'receptionTime'],
            [Types.STRING(), Types.DOUBLE(), Types.DOUBLE(), Types.STRING()]
        )
        
        # Mock for JsonRowDeserializationSchema.builder()
        self.mock_builder = Mock()
        self.mock_builder.type_info.return_value = self.mock_builder
        self.mock_builder.build.return_value = Mock(spec=JsonRowDeserializationSchema)

    def test_init(self):
        # Test constructor with pram working
        adapter = JsonRowDeserializationAdapter(self.sample_type_info)
        self.assertEqual(adapter._JsonRowDeserializationAdapter__row_type_info, self.sample_type_info)
    
    @patch('Core.JsonRowDeserializationAdapter.JsonRowDeserializationSchema.builder')
    def test_get_deserialization_schema(self, mock_schema_builder):
        # configure the mock of JsonRowDeserializationSchema.builder() to return our mock_builder
        mock_schema_builder.return_value = self.mock_builder
        
        # create adapter
        adapter = JsonRowDeserializationAdapter(self.sample_type_info)
        
        # call method to test
        result = adapter.get_deserialization_schema()
        
        # verify method has been called
        mock_schema_builder.assert_called_once()
        
        # Verify that type_info has been called with the correct parameter
        self.mock_builder.type_info.assert_called_once_with(self.sample_type_info)
        
        # verify final method build has been called
        self.mock_builder.build.assert_called_once()
        
        # Verify that the result is the expected one
        self.assertEqual(result, self.mock_builder.build.return_value)