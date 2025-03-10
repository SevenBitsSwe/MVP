from Models.IUserRepository import IUserRepository
from Models.DatabaseConnection import DatabaseConnection
from Models.UserDAO import UserDAO
import uuid

class UserRepository(IUserRepository):
    def __init__(self, db_connection: DatabaseConnection):
        self.__db_conn = db_connection

    def mark_user_as_occupied(self, user_uuid: uuid.UUID, sensor_uuid: uuid.UUID):
        """Marks a user as occupied in the database"""
        query = f"ALTER TABLE nearyou.user UPDATE assigned_sensor_uuid = '{sensor_uuid}' WHERE user_uuid = '{user_uuid}'"
        conn = self.__db_conn.connect()
        result = conn.query(query)

    def get_free_user(self) -> UserDAO:
        """Retrieves first user without a sensor from the database"""
        query = "SELECT user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status FROM nearyou.user WHERE assigned_sensor_uuid IS NULL"
        conn = self.__db_conn.connect()
        result = conn.query(query)

        if not result.result_rows:
            return None
        user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status = result.result_rows[0]
        return UserDAO(user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status)