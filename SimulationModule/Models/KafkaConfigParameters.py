from dataclasses import dataclass


@dataclass
class KafkaConfigParameters:
    bootstrap_servers: str = "kafka:9092"
    source_topic: str = "SimulatorPosition"
    