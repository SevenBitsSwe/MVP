import uuid

class SensorDTO:
    '''This class is a Data Access Object for the Sensor class. It is used to abstract the sensor'''

    def __init__(self, sensor_uuid: uuid, is_occupied: bool):
        '''constructor to initialize the sensor data access object'''
        self.sensor_uuid = sensor_uuid
        self.is_occupied = is_occupied
