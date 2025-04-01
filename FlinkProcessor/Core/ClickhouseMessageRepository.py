from Core.IMessageRepository import IMessageRepository
from Core.DatabaseConnection import DatabaseConnection
from Core.MessageDTO import MessageDTO

class ClickhouseMessageRepository(IMessageRepository):

    def __init__(self, db_connection: DatabaseConnection):
        self.__db_conn = db_connection

    def check_activity_already_displayed_for_user(self, user_id : str,activity_id : str) -> bool:
        param = {'user_id':user_id,'activity_id':activity_id}
        query = '''
        SELECT 
        user_uuid as user_id,
        activity_uuid as activity_id
        FROM nearyou.messageTable
        WHERE user_uuid = %(user_id)s AND activity_uuid = %(activity_id)s
        '''
        conn = self.__db_conn.connect()
        dizionario = conn.query(query, parameters=param)
        if len(dizionario.result_set) == 0:
            return False
        else:
            return True
