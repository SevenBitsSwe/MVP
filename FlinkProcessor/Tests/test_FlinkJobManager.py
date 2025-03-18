import pytest
from unittest.mock import Mock, patch, ANY
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.functions import MapFunction, FilterFunction
from pyflink.common import Types
from pyflink.common.watermark_strategy import WatermarkStrategy

from Core.IPositionReceiver import IPositionReceiver
from Core.IMessageWriter import IMessageWriter
from Core.FlinkJobManager import FlinkJobManager
from Core.KafkaWriterConfiguration import KafkaWriterConfiguration

class TestFlinkJobManager:
    
    @pytest.fixture
    def mock_env(self):
        env_mock = Mock(spec=StreamExecutionEnvironment)
        return env_mock
    
    @pytest.fixture
    def mock_map_function(self):
        map_function_mock = Mock(spec=MapFunction)
        return map_function_mock
    
    @pytest.fixture
    def mock_filter_function(self):
        filter_function_mock = Mock(spec=FilterFunction)
        return filter_function_mock
    
    @pytest.fixture
    def mock_position_receiver(self):
        position_receiver_mock = Mock(spec=IPositionReceiver)
        position_receiver_mock.get_position_receiver.return_value = Mock()
        return position_receiver_mock
    
    @pytest.fixture
    def mock_message_writer(self):
        message_writer_mock = Mock(spec=IMessageWriter)
        message_writer_mock.get_message_writer.return_value = Mock()
        return message_writer_mock
    
    @pytest.fixture
    def mock_datastream(self):
        datastream_mock = Mock()
        return datastream_mock
    
    @pytest.fixture
    def mock_keyed_stream(self):
        keyed_stream_mock = Mock()
        return keyed_stream_mock
    
    @pytest.fixture
    def mock_mapped_stream(self):
        mapped_stream_mock = Mock()
        return mapped_stream_mock
    
    @pytest.fixture
    def mock_filtered_stream(self):
        filtered_stream_mock = Mock()
        return filtered_stream_mock
    
    def test_initialization(self, mock_env, mock_map_function, mock_filter_function, 
                           mock_position_receiver, mock_message_writer,
                           mock_datastream, mock_keyed_stream, mock_mapped_stream, 
                           mock_filtered_stream):
        # Configure mock behavior
        mock_env.from_source.return_value = mock_datastream
        mock_datastream.key_by.return_value = mock_keyed_stream
        mock_keyed_stream.map.return_value = mock_mapped_stream
        mock_mapped_stream.filter.return_value = mock_filtered_stream
        
        # Create instance to test
        job_manager = FlinkJobManager(
            mock_env,
            mock_map_function,
            mock_filter_function,
            mock_position_receiver,
            mock_message_writer
        )
        
        # Verify that the methods were called correctly
        mock_env.from_source.assert_called_once_with(
            mock_position_receiver.get_position_receiver(),
            ANY,  # Use ANY instead of pytest.approx(match=True)
            "Positions Source"
        )
        mock_datastream.key_by.assert_called_once()
        mock_keyed_stream.map.assert_called_once_with(
            mock_map_function,
            output_type=KafkaWriterConfiguration().row_type_info_message
        )
        mock_mapped_stream.filter.assert_called_once_with(mock_filter_function)
        mock_filtered_stream.sink_to.assert_called_once_with(mock_message_writer.get_message_writer())
        
    def test_execute(self, mock_env, mock_map_function, mock_filter_function,
                    mock_position_receiver, mock_message_writer,
                    mock_datastream, mock_keyed_stream, mock_mapped_stream, 
                    mock_filtered_stream):
        # Configure mock behavior
        mock_env.from_source.return_value = mock_datastream
        mock_datastream.key_by.return_value = mock_keyed_stream
        mock_keyed_stream.map.return_value = mock_mapped_stream
        mock_mapped_stream.filter.return_value = mock_filtered_stream
        
        # Create instance to test
        job_manager = FlinkJobManager(
            mock_env,
            mock_map_function,
            mock_filter_function,
            mock_position_receiver,
            mock_message_writer
        )
        
        # Call method to test
        job_manager.execute()
        
        # Verify that the execute method of the environment was called
        mock_env.execute.assert_called_once_with("Flink Job")