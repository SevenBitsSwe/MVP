import time
from Core.FlinkJobManager import FlinkJobManager
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.execution_mode import RuntimeExecutionMode
from pyflink.datastream.functions import MapFunction,FilterFunction
from pyflink.common.watermark_strategy import WatermarkStrategy
from Core.IPositionReceiver import IPositionReceiver
from Core.IMessageWriter import IMessageWriter
from Core.KafkaMessageWriter import KafkaMessageWriter
from Core.KafkaPositionReceiver import KafkaPositionReceiver
from Core.KafkaSourceConfiguration import KafkaSourceConfiguration
from Core.KafkaWriterConfiguration import KafkaWriterConfiguration
from Core.JsonRowDeserializationAdapter import JsonRowDeserializationAdapter
from Core.JsonRowSerializationAdapter import JsonRowSerializationAdapter
from Core.PositionToMessageProcessor import PositionToMessageProcessor
from Core.FilterMessageAlreadyDisplayed import FilterMessageAlreadyDisplayed
from Core.LLMService import LLMService
from Core.StructuredResponseMessage import StructuredResponseMessage
from Core.GroqLLMService import GroqLLMService
from pyflink.common import Configuration

config = Configuration()
config.set_string("python.execution-mode", "thread")
config.set_boolean("python.operator-chaining.enabled", False)
config.set_integer("python.fn-execution.bundle.size", 200)
config.set_integer("python.fn-execution.bundle.time", 800)


time.sleep(9)
streaming_env = StreamExecutionEnvironment.get_execution_environment(config)

streaming_env.add_jars("file:///opt/flink/usrlib/flink-sql-connector-kafka-3.2.0-1.18.jar")
streaming_env.set_parallelism(10)
streaming_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)

serialization_adapter = JsonRowSerializationAdapter(KafkaWriterConfiguration().row_type_info_message)
deserialization_adapter = JsonRowDeserializationAdapter(KafkaSourceConfiguration().row_type)

llm_service_istance: LLMService = GroqLLMService(StructuredResponseMessage)

map_function_istance: MapFunction = PositionToMessageProcessor(llm_service_istance)
filter_function_istance: FilterFunction = FilterMessageAlreadyDisplayed()
position_receiver_istance: IPositionReceiver = KafkaPositionReceiver(KafkaSourceConfiguration(),deserialization_adapter)
message_writer_istance: IMessageWriter = KafkaMessageWriter(KafkaWriterConfiguration(),serialization_adapter)


job_istance = FlinkJobManager(
    streaming_env,
    map_function_istance,
    filter_function_istance,
    position_receiver_istance,
    message_writer_istance
)

job_istance.execute()