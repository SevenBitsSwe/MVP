from dataclasses import dataclass
from pyflink.common import Types

@dataclass
class KafkaWriterConfiguration:
    bootstrap_servers: str = "kafka:9092"
    writable_topic: str = "MessageElaborated"
    key_type = Types.ROW_NAMED(
                                ['user_uuid'],  # i campi principali
                                [
                                    Types.STRING()
                                ])
    row_type_info_message = Types.ROW_NAMED(
                                            ['user_uuid', 'activity_uuid', 'message_uuid','message','activityLatitude','activityLongitude','creationTime','userLatitude','userLongitude'],
                                            [
                                                Types.STRING(),
                                                Types.STRING(),
                                                Types.STRING(),
                                                Types.STRING(),
                                                Types.FLOAT(),
                                                Types.FLOAT(),
                                                Types.STRING(),
                                                Types.FLOAT(),
                                                Types.FLOAT()
                                            ]
                                            )
