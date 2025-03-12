from dataclasses import dataclass
from pyflink.common import Types
from pyflink.common.types import Row

@dataclass
class KafkaWriterConfiguration:
    bootstrap_servers: str = "kafka:9092"
    writable_topic: str = "MessageElaborated"
    key_type = Types.ROW_NAMED(
                                ['id'],  # i campi principali
                                [
                                    Types.STRING()
                                ])
    row_type_info_message = Types.ROW_NAMED(
                                            ['id', 'message', 'latitude','longitude','creationTime'],  # i campi principali
                                            [
                                                Types.STRING(),
                                                Types.STRING(),
                                                Types.FLOAT(),  
                                                Types.FLOAT(),
                                                Types.STRING()
                                            ]
                                            )