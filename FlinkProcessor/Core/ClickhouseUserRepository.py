from Core.IUserRepository import IUserRepository
from Core.DatabaseConnection import DatabaseConnection
from Core.UserDTO import UserDTO

class ClickhouseUserRepository(IUserRepository):
    def __init__(self, db_connection: DatabaseConnection):
        self.__db_conn = db_connection

    def get_user_who_owns_sensor(self, sensor_uuid) -> UserDTO:
        """Retrieves the user who owns a sensor from the database"""
        params = {
            "sensor_uuid": sensor_uuid
        }
        conn = self.__db_conn.connect()
        query = """
                SELECT 
                    user.user_uuid, 
                    user.assigned_sensor_uuid, 
                    user.name, 
                    user.surname, 
                    user.email, 
                    user.gender, 
                    user.birthdate, 
                    user.civil_status, 
                    groupArray(u.interest) as interests
                FROM nearyou.user 
                INNER JOIN nearyou.user_interest as u on user.user_uuid = u.user_uuid  
                WHERE user.assigned_sensor_uuid = %(sensor_uuid)s  
                GROUP BY 
                    user.user_uuid, 
                    user.assigned_sensor_uuid, 
                    user.name, 
                    user.surname, 
                    user.email, 
                    user.gender, 
                    user.birthdate, 
                    user.civil_status
                """
        result = conn.query(query, parameters=params)

        if not result.result_rows:
            return None
        user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status, interest_list = result.result_rows[0]
        return UserDTO(user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status, interest_list)
