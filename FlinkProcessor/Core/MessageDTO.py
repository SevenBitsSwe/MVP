import uuid

class MessageDTO:
    '''This class is a Data Transfer Object for the User class. It is used to abstract the user'''

    def __init__(self,
                 user_id: uuid = uuid.uuid4(),
                 activity_id: uuid = uuid.uuid4(),
                 message_id: uuid = uuid.uuid4(),
                 message_text: str = "",
                 activity_lat: float = 0.0,
                 activity_lon: float = 0.0,
                 creation_time: str = "",
                 user_lat: float = 0.0,
                 user_lon: float = 0.0):
        '''constructor to initialize the user data access object'''
        self.user_id = str(user_id)
        self.activity_id = str(activity_id)
        self.message_id = str(message_id)
        self.message_text = message_text
        self.activity_lat = activity_lat
        self.activity_lon = activity_lon
        self.creation_time = creation_time
        self.user_lat = user_lat
        self.user_lon = user_lon
    

       