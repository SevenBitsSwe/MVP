import time
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.execution_mode import RuntimeExecutionMode
from pyflink.datastream.functions import MapFunction,FilterFunction
from pyflink.common import Configuration
from Core.FlinkJobManager import FlinkJobManager
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
from Core.FilterMessageValidator import FilterMessageValidator
from Core.LLMService import LLMService
from Core.StructuredResponseMessage import StructuredResponseMessage
from Core.GroqLLMService import GroqLLMService


from Core.IUserRepository import IUserRepository
from Core.IActivityRepository import IActivityRepository
from Core.IMessageRepository import IMessageRepository
from Core.ClickhouseUserRepository import ClickhouseUserRepository
from Core.ClickhouseActivityRepository import ClickhouseActivityRepository
from Core.ClickhouseMessageRepository import ClickhouseMessageRepository
from Core.DatabaseConnection import DatabaseConnection
from Core.DatabaseConfigParameters import DatabaseConfigParameters
from Core.IFlinkSerializable import IFlinkSerializable
from Core.MessageSerializer import MessageSerializer

config = Configuration()
config.set_string("python.execution-mode", "thread")
# config.set_boolean("python.operator-chaining.enabled", False)
# config.set_integer("python.fn-execution.bundle.size", 200)
# config.set_integer("python.fn-execution.bundle.time", 800)


time.sleep(9)
streaming_env = StreamExecutionEnvironment.get_execution_environment(config)

streaming_env.add_jars("file:///opt/flink/usrlib/flink-sql-connector-kafka-3.2.0-1.18.jar")
streaming_env.set_parallelism(10)
streaming_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)

serialization_adapter = JsonRowSerializationAdapter(KafkaWriterConfiguration().row_type_info_message)
deserialization_adapter = JsonRowDeserializationAdapter(KafkaSourceConfiguration().row_type)

llm_service_istance: LLMService = GroqLLMService(StructuredResponseMessage)
db_connection = DatabaseConnection(DatabaseConfigParameters())
user_repository : IUserRepository = ClickhouseUserRepository(db_connection)
activity_repository: IActivityRepository = ClickhouseActivityRepository(db_connection)
message_repository: IMessageRepository = ClickhouseMessageRepository(db_connection)
message_serializer: IFlinkSerializable = MessageSerializer()

map_function_istance: MapFunction = PositionToMessageProcessor(llm_service_istance,user_repository, activity_repository,message_serializer)
filter_validator_istance: FilterFunction = FilterMessageValidator()
filter_function_istance: FilterFunction = FilterMessageAlreadyDisplayed(message_repository)
position_receiver_istance: IPositionReceiver = KafkaPositionReceiver(KafkaSourceConfiguration(),deserialization_adapter)
message_writer_istance: IMessageWriter = KafkaMessageWriter(KafkaWriterConfiguration(),serialization_adapter)


job_istance = FlinkJobManager(
    streaming_env,
    map_function_istance,
    filter_validator_istance,
    filter_function_istance,
    position_receiver_istance,
    message_writer_istance
)

job_istance.execute()
