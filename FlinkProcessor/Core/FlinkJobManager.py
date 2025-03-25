from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.functions import MapFunction,FilterFunction
from pyflink.common.watermark_strategy import WatermarkStrategy
from pyflink.common import Types
from Core.IPositionReceiver import IPositionReceiver
from Core.IMessageWriter import IMessageWriter
from Core.KafkaWriterConfiguration import KafkaWriterConfiguration

class FlinkJobManager:
    def __init__(self,
                 streaming_env_istance : StreamExecutionEnvironment,
                 map_function_implementation : MapFunction,
                 filter_function_implementation : FilterFunction,
                 position_receiver_istance: IPositionReceiver,
                 message_sender_istance: IMessageWriter
                 ):
        self.__streaming_env = streaming_env_istance
        self.__populated_datastream = self.__streaming_env.from_source(position_receiver_istance.get_position_receiver(),
                                                                   WatermarkStrategy.for_monotonous_timestamps(),
                                                                   "Positions Source")
        self.keyed_stream = self.__populated_datastream.key_by(lambda x: x[0], key_type=Types.STRING())

        self.__mapped_stream = self.keyed_stream.map(map_function_implementation,output_type=KafkaWriterConfiguration().row_type_info_message)

        self.__filtered_stream = self.__mapped_stream.filter(filter_function_implementation)
        self.__filtered_stream.sink_to(message_sender_istance.get_message_writer())

    def execute(self):
        self.__streaming_env.execute("Flink Job")
