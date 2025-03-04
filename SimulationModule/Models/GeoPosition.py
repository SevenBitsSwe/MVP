class GeoPosition:
    '''Class representing a position in the world,with the sensor id with latitude and longitude,
    and timestamp of the position'''
    def __init__(self, sensor_id: str, latitude: float, longitude: float, timestamp: str):
        '''constructor to initialize the position'''
        self.__sensor_id = sensor_id
        self.__latitude = latitude
        self.__longitude = longitude
        self.__timestamp = timestamp
        