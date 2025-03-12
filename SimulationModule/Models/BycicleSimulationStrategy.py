from Models.IPositionSimulationStrategy import IPositionSimulationStrategy
from Models.GpsSensor import GpsSensor
from Models.GeoPosition import GeoPosition
from datetime import datetime
from SimulationModule.Models.SensorSubject import SensorSubject
import osmnx
import random

class BycicleSimulationStrategy(IPositionSimulationStrategy):

    def __init__(self):
        '''constructor to initialize the bycicle simulation strategy'''
        self.__bycicle_speed_approximated = 15
        self.__delta_time_between_positions = 10

    def get_route(self, graph_istance) -> list:
        '''method to simulate the position live update'''
        graph_returned = graph_istance
        graph_nodes = list(graph_returned.nodes)
        starting_node = random.choice(graph_nodes)
        destination_node = random.choice(graph_nodes)

        shortest_route = osmnx.shortest_path(
            graph_returned,
            starting_node,
            destination_node,
            weight='length'
        )
        route_coords = [(graph_returned.nodes[node]["y"], graph_returned.nodes[node]["x"]) for node in shortest_route]

        return route_coords


    def get_delta_time(self) -> float:
        return self.__delta_time_between_positions

    def get_speed(self) -> float:
        speed = self.__bycicle_speed_approximated / 3.6
        return speed

