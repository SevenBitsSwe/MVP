from Core.IMessageRepository import IMessageRepository
from Core.DatabaseConnection import DatabaseConnection
from Core.MessageDTO import MessageDTO

class ClickhouseMessageRepository(IMessageRepository):

    def __init__(self, db_connection: DatabaseConnection):
        self.__db_conn = db_connection

    # def get_user_last_message(self, user_id) -> MessageDTO:
    #     param = {'user_id':user_id}
    #     query= '''
    #     SELECT 
    #     user_uuid as user_idd,
    #     activity_uuid as activity_id,
    #     message_uuid as message_id,
    #     message as message_text,
    #     activityLatitude as latitude,
    #     activityLongitude as longitude,
    #     creationTime as creation_time,
    #     userLatitude as user_lat,
    #     userLongitude as user_lon
    #     FROM nearyou.messageTable
    #     WHERE user_uuid = %(user_id)s
    #     ORDER BY creationTime DESC LIMIT 1
    #     '''
    #     conn = self.__db_conn.connect()
    #     dizionario = conn.query(query, parameters=param)
    #     if len(dizionario.result_set) == 0:
    #         return MessageDTO()
    #     else:
    #         return MessageDTO(user_id=dizionario.first_item['user_idd'],
    #                           activity_id=dizionario.first_item['activity_id'],
    #                           message_id=dizionario.first_item['message_id'],
    #                           message_text=dizionario.first_item['message_text'],
    #                           activity_lat=float(dizionario.first_item['latitude']),
    #                           activity_lon=float(dizionario.first_item['longitude']),
    #                           creation_time=dizionario.first_item['creation_time'],
    #                           user_lat=float(dizionario.first_item['user_lat']),
    #                           user_lon=float(dizionario.first_item['user_lon']))
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