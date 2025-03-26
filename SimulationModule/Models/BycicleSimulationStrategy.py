from Models.IPositionSimulationStrategy import IPositionSimulationStrategy
from Models.GraphWrapper import GraphWrapper
import osmnx
import random

class BycicleSimulationStrategy(IPositionSimulationStrategy):

    def __init__(self, graph_istance: GraphWrapper):
        '''constructor to initialize the bycicle simulation strategy'''
        self.__bycicle_speed_approximated = 15
        self.__delta_time_between_positions = 21
        self.__graph_istance = graph_istance.get_graph()

    def get_route(self):
        '''method to simulate the position live update'''
        graph_returned = self.__graph_istance
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

