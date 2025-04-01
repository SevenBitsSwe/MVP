import uuid
from Models.ISensorRepository import ISensorRepository
from Models.DatabaseConnection import DatabaseConnection
from Models.SensorDTO import SensorDTO

class SensorRepository(ISensorRepository):
    def __init__(self, db_connection: DatabaseConnection):
        self.__db_conn = db_connection

    def mark_sensor_as_occupied(self, sensor_uuid: uuid.UUID):
        """Marks a sensor as occupied in the database"""
        query = f"ALTER TABLE nearyou.sensor UPDATE is_occupied = true WHERE sensor_uuid = '{sensor_uuid}'"
        conn = self.__db_conn.connect()
        conn.query(query)
        self.__db_conn.disconnect()

    def get_non_occupied_sensor(self) -> SensorDTO:
        """Retrieves first non occupied sensor from the database"""
        query = "SELECT sensor_uuid, is_occupied FROM nearyou.sensor WHERE is_occupied = 0"
        conn = self.__db_conn.connect()
        result = conn.query(query)
        self.__db_conn.disconnect()

        if not result.result_rows:
            print("No non occupied sensors found")
            return None
        sensor_uuid, is_occupied = result.result_rows[0]
        return SensorDTO(sensor_uuid, bool(is_occupied))
