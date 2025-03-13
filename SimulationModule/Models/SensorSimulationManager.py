from multiprocessing.pool import ThreadPool

class SensorSimulationManager:
    '''This class implements all the logic to simulate the sensors and send the data to a Kafka topic'''
    def __init__(self, list_of_sensors: list["SensorSubject"]):
        '''constructor to initialize the sensor simulation manager'''
        self.__sensor_registry = list_of_sensors

    def start_simulation(self):
        '''method to start the simulation'''

        with ThreadPool(len(self.__sensor_registry)) as pool:
            pool.map(lambda sensor: sensor.simulate(), self.__sensor_registry)
            
