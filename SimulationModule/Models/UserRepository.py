import clickhouse_connect
from Models.IUserRepository import IUserRepository
from Models.DatabaseConfig import DatabaseConfig
from Models.UserDAO import UserDAO
import uuid

class UserRepository(IUserRepository):
    def __init__(self):
        self.__db_config = DatabaseConfig.load_config()
        self.__connection = None

    def connect(self):
        self.__connection = clickhouse_connect.get_client(
            host=self.__db_config.host,
            port=self.__db_config.port,
            user=self.__db_config.user,
            password=self.__db_config.password
        )
        return self.__connection

    def mark_user_as_occupied(self, user_uuid: uuid.UUID, sensor_uuid: uuid.UUID):
        """Marks a user as occupied in the database"""
        query = f"ALTER TABLE nearyou.user UPDATE assigned_sensor_uuid = '{sensor_uuid}' WHERE user_uuid = '{user_uuid}'"
        conn = self.connect()
        result = conn.query(query)

    def get_free_user(self) -> UserDAO:
        """Retrieves first user without a sensor from the database"""
        query = "SELECT user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status FROM nearyou.user WHERE assigned_sensor_uuid IS NULL"
        conn = self.connect()
        result = conn.query(query)

        if not result.result_rows:
            return None
        user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status = result.result_rows[0]
        return UserDAO(user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status)