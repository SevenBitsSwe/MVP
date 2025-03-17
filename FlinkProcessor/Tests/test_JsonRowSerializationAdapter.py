import unittest
from unittest.mock import Mock, patch, MagicMock

from pyflink.common import Types
from pyflink.datastream.formats.json import JsonRowSerializationSchema
from Core.JsonRowSerializationAdapter import JsonRowSerializationAdapter

class TestJsonRowSerializationAdapter(unittest.TestCase):
    
    def setUp(self):
        # Create type info as position schema
        self.sample_type_info = Types.ROW_NAMED(
            ['user_uuid', 'activity_uuid', 'message_uuid','message','activityLatitude','activityLongitude','creationTime','userLatitude','userLongitude'],
            [Types.STRING(), Types.STRING(), Types.STRING(), Types.STRING(), Types.FLOAT(), Types.FLOAT(), Types.STRING(), Types.FLOAT(), Types.FLOAT()]
        )
        
        # Mock for JsonRowSerializationSchema.builder()
        self.mock_builder = Mock()
        self.mock_builder.with_type_info.return_value = self.mock_builder
        self.mock_builder.build.return_value = Mock(spec=JsonRowSerializationSchema)

    def test_init(self):
        # Test constructor with param working
        adapter = JsonRowSerializationAdapter(self.sample_type_info)
        self.assertEqual(adapter._JsonRowSerializationAdapter__row_type_info_message, self.sample_type_info)
    
    @patch('Core.JsonRowSerializationAdapter.JsonRowSerializationSchema.builder')
    def test_get_serialization_schema(self, mock_schema_builder):
        # configure the mock of JsonRowSerializationSchema.builder() to return our mock_builder
        mock_schema_builder.return_value = self.mock_builder
        
        # create adapter
        adapter = JsonRowSerializationAdapter(self.sample_type_info)
        
        # call method to test
        result = adapter.get_serialization_schema()
        
        # verify method has been called
        mock_schema_builder.assert_called_once()
        
        # Verify that with_type_info has been called with the correct parameter
        self.mock_builder.with_type_info.assert_called_once_with(self.sample_type_info)
        
        # verify final method build has been called
        self.mock_builder.build.assert_called_once()
        
        # Verify that the result is the expected one
        self.assertEqual(result, self.mock_builder.build.return_value)