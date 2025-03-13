from Core.IMessageRepository import IMessageRepository
from Core.DatabaseConnection import DatabaseConnection
from Core.UserDTO import UserDTO
import uuid

class ClickhouseMessageRepository(IMessageRepository):

    def __init__(self, db_connection: DatabaseConnection):
        self.__db_conn = db_connection

    def get_user_last_message(self, user_id) -> dict:
            param = {'user_id':user_id}
            query= '''
            SELECT 
                activityLongitude as longitude,
                activityLatitude as latitude
            FROM nearyou.messageTable
            WHERE user_uuid = %(user_id)s
            ORDER BY creationTime DESC LIMIT 1
            '''    
            conn = self.__db_conn.connect()
            dizionario = conn.query(query, parameters=param)
            if len(dizionario.result_set) == 0:
                return {"longitude" : 0, "latitude" : 0}
            else: return dizionario.first_item