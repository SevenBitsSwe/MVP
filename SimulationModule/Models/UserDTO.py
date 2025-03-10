import uuid

class UserDTO:
    '''This class is a Data Access Object for the User class. It is used to abstract the user'''

    def __init__(self, user_uuid: uuid, assigned_sensor_uuid: uuid, name: str, surname: str, email: str, gender: str, birthdate: str, civil_status: str):
        '''constructor to initialize the user data access object'''
        self.user_uuid = user_uuid
        self.assigned_sensor_uuid = assigned_sensor_uuid
        self.name = name
        self.surname = surname
        self.email = email
        self.gender = gender
        self.birthdate = birthdate
        self.civil_status = civil_status
