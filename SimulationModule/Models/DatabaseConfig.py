from Models.DatabaseConfigParameters import DatabaseConfigParameters
import json
from pathlib import Path

class DatabaseConfig:
    def __init__(self, config_parameters: DatabaseConfigParameters):
        self.host = config_parameters.host
        self.port = config_parameters.port
        self.user = config_parameters.user
        self.password = config_parameters.password