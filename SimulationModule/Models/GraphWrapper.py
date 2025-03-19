import osmnx

class GraphWrapper:
    ''' This class  hides the implementation of a graph wiht osmnx'''

    def __init__(self,latitude: float, longitude: float, map_radius: int, network_type: str):
        '''constructor to initialize the graph wrapper'''
        self.__latitude = latitude
        self.__longitude = longitude
        self.__map_radius = map_radius
        self.__network_type = network_type

    def get_graph(self) -> osmnx.graph:
        '''method to get the graph'''
        return osmnx.graph_from_point(
            (self.__latitude, self.__longitude),
            dist=self.__map_radius,
            network_type=self.__network_type
        )
