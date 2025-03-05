from Models.SensorSimulationManager import SensorSimulationManager
from Models.PositionJsonAdapter import PositionJsonAdapter
from Models.KafkaConfluentAdapter import KafkaConfluentAdapter
from Models.KafkaConfigParameters import KafkaConfigParameters
from Models.IPositionSimulationStrategy import IPositionSimulationStrategy
from Models.BycicleSimulationStrategy import BycicleSimulationStrategy
from Models.GraphWrapper import GraphWrapper
from confluent_kafka import Producer
print("Starting simulation")

json_adapter: PositionJsonAdapter = PositionJsonAdapter()
kafka_confluent_adapter = KafkaConfluentAdapter(
                                                KafkaConfigParameters(),
                                                json_adapter,
                                                Producer({'bootstrap.servers': KafkaConfigParameters().bootstrap_servers})
                                                )
strategy_simulation : IPositionSimulationStrategy = BycicleSimulationStrategy()
map_graph = GraphWrapper(45.3, 11.87, 4000, 'walk')




sensor_simulation_istance = SensorSimulationManager(10, kafka_confluent_adapter, strategy_simulation,map_graph)
sensor_simulation_istance.start_simulation()




