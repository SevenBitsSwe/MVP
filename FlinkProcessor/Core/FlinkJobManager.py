from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.execution_mode import RuntimeExecutionMode
from pyflink.datastream.functions import MapFunction,FilterFunction
from pyflink.common.watermark_strategy import WatermarkStrategy
from Core.IpositionReceiver import IpositionReceiver
from Core.IMessageWriter import IMessageWriter

class FlinkJobManager : 
    def __init__(self,
                 streaming_env_istance : StreamExecutionEnvironment,
                 map_function_implementation : MapFunction,
                 filter_function_implementation : FilterFunction,
                 position_receiver_istance: IpositionReceiver,
                 message_sender_istance: IMessageWriter
                 ):
        self.__streaming_env = streaming_env_istance
        self.__populated_datastream = self.__streaming_env.from_source(position_receiver_istance.get_position_receiver(),
                                                                   WatermarkStrategy.for_monotonous_timestamps(),
                                                                   "Positions Source")
        self.__mapped_stream = self.__populated_datastream.map(map_function_implementation)
        self.__filtered_stream = self.__mapped_stream.filter(filter_function_implementation)
        self.__filtered_stream.sink_to(message_sender_istance.get_message_writer())
        self.__streaming_env.execute("Position Elaboration Job")
