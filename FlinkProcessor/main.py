import time
from FlinkJobManager import FlinkJobManager
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.execution_mode import RuntimeExecutionMode
from pyflink.datastream.functions import MapFunction,FilterFunction
from pyflink.common.watermark_strategy import WatermarkStrategy
from Core.IpositionReceiver import IpositionReceiver
from Core.IMessageWriter import IMessageWriter
from Core.KafkaMessageWriter import KafkaMessageWriter
from Core.KafkaPositionReceiver import KafkaPositionReceiver
from Core.KafkaSourceConfiguration import KafkaSourceConfiguration
from Core.KafkaWriterConfiguration import KafkaWriterConfiguration
from Core.JsonRowDeserializationAdapter import JsonRowDeserializationAdapter
from Core.JsonRowSerializationAdapter import JsonRowSerializationAdapter

time.sleep(9)
streaming_env = StreamExecutionEnvironment.get_execution_environment()
streaming_env.add_jars("file:///opt/flink/usrlib/flink-sql-connector-kafka-3.2.0-1.18.jar")
streaming_env.set_parallelism(1)
streaming_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)

serialization_adapter = JsonRowSerializationAdapter(KafkaWriterConfiguration().row_type_info_message)
deserialization_adapter = JsonRowDeserializationAdapter(KafkaSourceConfiguration().row_type)

map_function_istance: MapFunction = MapFunction()
filter_function_istance: FilterFunction = FilterFunction()
position_receiver_istance: IpositionReceiver = KafkaPositionReceiver(KafkaSourceConfiguration(),serialization_adapter)
message_writer_istance: IMessageWriter = KafkaMessageWriter(KafkaWriterConfiguration(),deserialization_adapter)


job_istance = FlinkJobManager(
    streaming_env,
    map_function_istance,
    filter_function_istance,
    position_receiver_istance,
    message_writer_istance
)

job_istance.execute()