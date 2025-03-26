from Models.SensorSimulationAdministrator import SensorSimulationAdministrator
from Models.PositionJsonAdapter import PositionJsonAdapter
from Models.PositionSender import PositionSender
from Models.KafkaConfluentAdapter import KafkaConfluentAdapter
from Models.KafkaConfigParameters import KafkaConfigParameters
from Models.IPositionSimulationStrategy import IPositionSimulationStrategy
from Models.BycicleSimulationStrategy import BycicleSimulationStrategy
from Models.GraphWrapper import GraphWrapper
from Models.SensorFactory import SensorFactory
from Models.SensorRepository import SensorRepository
from Models.UserRepository import UserRepository
from Models.ISensorRepository import ISensorRepository
from Models.IUserRepository import IUserRepository
from Models.DatabaseConnection import DatabaseConnection
from Models.DatabaseConfigParameters import DatabaseConfigParameters
from confluent_kafka import Producer

print("Starting simulation")

json_adapter: PositionJsonAdapter = PositionJsonAdapter()
kafka_confluent_adapter : PositionSender = KafkaConfluentAdapter(
                                                KafkaConfigParameters(),
                                                json_adapter,
                                                Producer({'bootstrap.servers': KafkaConfigParameters().bootstrap_servers})
                                                )
map_graph = GraphWrapper(45.39, 11.87, 4000, 'walk')
strategy_simulation : IPositionSimulationStrategy = BycicleSimulationStrategy(map_graph)

db_connection = DatabaseConnection(DatabaseConfigParameters())
sensor_repository: ISensorRepository = SensorRepository(db_connection)
user_repository: IUserRepository = UserRepository(db_connection)
sensor_factory = SensorFactory(sensor_repository, user_repository)



sensor_simulation_istance = SensorSimulationAdministrator(sensor_factory.create_gps_sensor_list(kafka_confluent_adapter, strategy_simulation, 6))
sensor_simulation_istance.start_simulation()




