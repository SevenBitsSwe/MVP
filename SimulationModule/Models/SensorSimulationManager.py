from Models.SensorFactory import SensorFactory 
from Models.KafkaConfluentAdapter import KafkaConfluentAdapter
from Models.BycicleSimulationStrategy import BycicleSimulationStrategy
from Models.KafkaConfigParameters import KafkaConfigParameters
from Models.GraphWrapper import GraphWrapper    
from multiprocessing.pool import ThreadPool
import functools



class SensorSimulationManager:
    '''This class implements all the logic to simulate the sensors and send the data to a Kafka topic'''
    def __init__(self, number_of_sensors: int):
        '''constructor to initialize the sensor simulation manager'''
        self.__sensor_registry = []
        self.__number_of_sensors = number_of_sensors     
        self.__sensor_observer = KafkaConfluentAdapter(KafkaConfigParameters())
        self.__simulation_strategy = BycicleSimulationStrategy()

    def __populate_registry(self):
        '''method to populate the sensor registry with different types of sensors'''
        for i in range(self.__number_of_sensors):
            temporary_sensor = SensorFactory.create_gps_sensor()
            self.__sensor_registry.append(temporary_sensor)
            temporary_sensor.register_observer(self.__sensor_observer)


    def start_simulation(self):
        self.__populate_registry()
        '''method to start the simulation'''

        simulation_with_shared_graph = functools.partial(
            self.__simulation_strategy.simulate_position_live_update,
            graph_istance = GraphWrapper(45.3, 11.87, 4000, 'walk').get_graph()
        )
        with ThreadPool(self.__number_of_sensors) as pool:
            pool.map(simulation_with_shared_graph, self.__sensor_registry)
            