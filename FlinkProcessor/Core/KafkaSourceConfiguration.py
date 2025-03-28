from dataclasses import dataclass
from pyflink.common import Types

@dataclass
class KafkaSourceConfiguration:
    bootstrap_servers: str = "kafka:9092"
    source_topic: str = "SimulatorPosition"
    group_id: str = "pyflinkJob"
    enable_auto_commit: str = "true"
    commit_offsets_on_checkpoint: str = "true"
    row_type = Types.ROW_NAMED( ['user_uuid', 'latitude','longitude', 'received_at'],
                                [
                                    Types.STRING(),
                                    Types.FLOAT(),
                                    Types.FLOAT(),
                                    Types.STRING()
                                ])
