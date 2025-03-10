from Models.DatabaseConfigParameters import DatabaseConfigParameters
import json
from pathlib import Path
import clickhouse_connect

class DatabaseConnection:
    def __init__(self, config_parameters: DatabaseConfigParameters):
        self.host = config_parameters.host
        self.port = config_parameters.port
        self.user = config_parameters.user
        self.password = config_parameters.password
        self.connection = None

    def connect(self):
        self.connection = clickhouse_connect.get_client(
            host=self.host, 
            port=self.port, 
            user=self.user, 
            password=self.password
        )
        return self.connection

    def disconnect(self):
        self.connection.close()
        self.connection = None