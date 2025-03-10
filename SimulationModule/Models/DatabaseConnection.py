from Models.DatabaseConfigParameters import DatabaseConfigParameters
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
            username=self.user, 
            password=self.password
        )
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
