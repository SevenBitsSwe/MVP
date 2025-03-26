from dataclasses import dataclass

@dataclass
class DatabaseConfigParameters:
    host: str = "clickhouse"
    port: str = "8123"
    user: str = "default"
    password: str = "pass"
