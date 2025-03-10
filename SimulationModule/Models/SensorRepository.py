import clickhouse_connect
from Models.ISensorRepository import ISensorRepository
from Models.DatabaseConfig import DatabaseConfig
from Models.SensorDAO import SensorDAO
import uuid

class SensorRepository(ISensorRepository):
    def __init__(self, db_config: DatabaseConfig):
        self.__db_config = db_config
        self.__connection = None

    def connect(self):
        self.__connection = clickhouse_connect.get_client(
            host=self.__db_config.host,
            port=self.__db_config.port,
            user=self.__db_config.user,
            password=self.__db_config.password
        )
        return self.__connection

    def mark_sensor_as_occupied(self, sensor_uuid: uuid.UUID):
        """Marks a sensor as occupied in the database"""
        query = f"ALTER TABLE nearyou.sensor UPDATE is_occupied = true WHERE sensor_uuid = '{sensor_uuid}'"
        conn = self.connect()
        result = conn.query(query)

    def get_non_occupied_sensor(self) -> SensorDAO:
        """Retrieves first non occupied sensor from the database"""
        query = "SELECT sensor_uuid, is_occupied FROM nearyou.sensor WHERE is_occupied = 0"
        conn = self.connect()
        result = conn.query(query)

        if not result.result_rows:
            print("No non occupied sensors found")
            return None
        sensor_uuid, is_occupied = result.result_rows[0]
        return SensorDAO(sensor_uuid, bool(is_occupied))