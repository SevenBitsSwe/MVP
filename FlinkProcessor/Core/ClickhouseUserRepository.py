from Core.IUserRepository import IUserRepository
from Core.DatabaseConnection import DatabaseConnection
from Core.UserDTO import UserDTO
import uuid

class ClickhouseUserRepository(IUserRepository):
    def __init__(self, db_connection: DatabaseConnection):
        self.__db_conn = db_connection

    def mark_user_as_occupied(self, user_uuid: uuid.UUID, sensor_uuid: uuid.UUID):
        """Marks a user as occupied in the database"""
        query = f"ALTER TABLE nearyou.user UPDATE assigned_sensor_uuid = '{sensor_uuid}' WHERE user_uuid = '{user_uuid}'"
        conn = self.__db_conn.connect()
        result = conn.query(query)
        self.__db_conn.disconnect()

    def get_free_user(self) -> UserDTO:
        """Retrieves first user without a sensor from the database"""
        query = "SELECT user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status FROM nearyou.user WHERE assigned_sensor_uuid IS NULL"
        conn = self.__db_conn.connect()
        result = conn.query(query)
        self.__db_conn.disconnect()

        if not result.result_rows:
            return None
        user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status = result.result_rows[0]
        return UserDTO(user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status)

    def get_user_who_owns_sensor(self, sensor_uuid) -> UserDTO:
        """Retrieves the user who owns a sensor from the database"""
        params = {
            "sensor_uuid": sensor_uuid
        }
        query = "SELECT user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status FROM nearyou.user WHERE assigned_sensor_uuid = %(sensor_uuid)s"
        conn = self.__db_conn.connect()
        result = conn.query(query, parameters=params)

        if not result.result_rows:
            return None
        user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status = result.result_rows[0]
        return UserDTO(user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status)

    def get_user_last_message_coordinates(self, user_id) -> dict:
        param = {'user_id':user_id}
        query= '''
        SELECT 
            longitude,
            latitude
        FROM nearyou.messageTable
        WHERE id = %(user_id)s
        ORDER BY creationTime DESC LIMIT 1
        '''    
        conn = self.__db_conn.connect()
        dizionario = conn.query(query, parameters=param)
        if len(dizionario.result_set) == 0:
            return {"longitude" : 0, "latitude" : 0}
        else: return dizionario.first_item