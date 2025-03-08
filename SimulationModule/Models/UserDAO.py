import uuid

class UserDAO:
    '''This class is a Data Access Object for the User class. It is used to abstract the user'''

    def __init__(self, user_uuid: uuid, assigned_sensor_uuid: uuid, name: str, surname: str, email: str, gender: str, birthdate: str, civil_status: str):
        '''constructor to initialize the user data access object'''
        self._user_uuid = user_uuid
        self._assigned_sensor_uuid = assigned_sensor_uuid
        self._name = name
        self._surname = surname
        self._email = email
        self._gender = gender
        self._birthdate = birthdate
        self._civil_status = civil_status
