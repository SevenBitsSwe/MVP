import uuid

class ActivityDTO:
    '''This class is a Data Transfer Object for the User class. It is used to abstract the user'''

    def __init__(self, activity_id: uuid = uuid.uuid4(), activity_name: str = "",activity_lon: float = 0.0, activity_lat: float = 0.0, activity_addr: str ="", activity_type: str = "", activity_description: str =""):
        '''constructor to initialize the user data access object'''
        self.activity_id = activity_id
        self.activity_name = activity_name
        self.activity_lon = activity_lon
        self.activity_addr = activity_addr
        self.activity_lat = activity_lat
        self.activity_type = activity_type
        self.activity_description = activity_description
