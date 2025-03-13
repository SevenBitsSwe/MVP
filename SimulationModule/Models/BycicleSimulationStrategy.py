from Models.IPositionSimulationStrategy import IPositionSimulationStrategy
from Models.GpsSensor import GpsSensor
from Models.GeoPosition import GeoPosition
from datetime import datetime
from geopy.distance import geodesic
import time
import osmnx
import random

class BycicleSimulationStrategy(IPositionSimulationStrategy):

    def __init__(self):
        '''constructor to initialize the bycicle simulation strategy'''
        self.__bycicle_speed_approximated = 15
        self.__delta_time_between_positions = 20

    def simulate_position_live_update(self, sensor_istance: GpsSensor, graph_istance):
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

        speed_mps = self.__bycicle_speed_approximated / 3.6
        total_distance = 0
        for i in range(len(route_coords)-1):
            start_point = route_coords[i]
            end_point = route_coords[i+1]
            segment_distance = geodesic(start_point, end_point).meters
            total_distance += segment_distance
            num_positions = int(segment_distance / (speed_mps * self.__delta_time_between_positions))

            for j in range(num_positions):
                fraction = j / num_positions

                latitude = start_point[0] + fraction * (end_point[0] - start_point[0])
                longitude = start_point[1] + fraction * (end_point[1] - start_point[1])
                sensor_istance.set_current_position(
                    GeoPosition(
                        sensor_istance.get_sensor_uuid(),
                        float(latitude),
                        float(longitude),
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    )
                )
                time.sleep(self.__delta_time_between_positions)


