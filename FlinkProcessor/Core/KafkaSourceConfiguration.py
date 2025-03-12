from dataclasses import dataclass
from pyflink.common import Types
from pyflink.common.types import Row

@dataclass
class KafkaSourceConfiguration:
    bootstrap_servers: str = "kafka:9092"
    source_topic: str = "SimulatorPosition"
    group_id: str = "SimulatorGroup"
    enable_auto_commit: str = "true"
    commit_offsets_on_checkpoint: str = "true"
    row_type = Types.ROW_NAMED( ['id', 'latitude','longitude', 'receptionTime'],
                                [
                                    Types.STRING(), 
                                    Types.FLOAT(),  
                                    Types.FLOAT(),   
                                    Types.STRING()
                                    
                                ])