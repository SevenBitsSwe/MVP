import uuid

class SensorDAO:
    '''This class is a Data Access Object for the Sensor class. It is used to abstract the sensor'''

    def __init__(self, sensor_uuid: uuid, is_occupied: bool):
        '''constructor to initialize the sensor data access object'''
        self._sensor_uuid = sensor_uuid
        self._is_occupied = is_occupied