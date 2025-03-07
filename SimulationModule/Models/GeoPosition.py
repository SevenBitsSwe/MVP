class GeoPosition:
    '''Class representing a position in the world,with the sensor id with latitude and longitude,
    and timestamp of the position'''
    def __init__(self, sensor_id: str, latitude: float, longitude: float, timestamp: str):
        '''constructor to initialize the position'''
        self.__sensor_id = sensor_id
        self.__latitude = latitude
        self.__longitude = longitude
        self.__timestamp = timestamp
        
    def get_sensor_id(self) -> str:
        '''method to get the sensor id'''
        return str(self.__sensor_id)

    def get_latitude(self) -> float:
        '''method to get the latitude'''
        return self.__latitude      
    
    def get_longitude(self) -> float:       
        '''method to get the longitude'''
        return self.__longitude 
    
    def get_timestamp(self) -> str:
        '''method to get the timestamp'''
        return self.__timestamp 
    