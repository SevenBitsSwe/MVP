from Models.GraphWrapper import GraphWrapper
import osmnx
import unittest
from unittest.mock import MagicMock,patch


class TestGraphWrapper(unittest.TestCase):
    def setUp(self):
        self.latitude = 45.4668
        self.longitude = 9.1905
        self.map_radius = 4000
        self.network_type = "walk"
        
        self.graph_wrapper = GraphWrapper(
            self.latitude, 
            self.longitude, 
            self.map_radius, 
            self.network_type
        )

    def test_initialization(self):
        
        with patch('osmnx.graph_from_point') as mock_graph_from_point:
            self.graph_wrapper.get_graph()
            
            mock_graph_from_point.assert_called_once_with(
                (self.latitude, self.longitude),
                dist=self.map_radius,
                network_type=self.network_type
            )

    @patch('osmnx.graph_from_point')
    def test_get_graph(self, mock_graph_from_point):
        mock_graph = MagicMock()
        mock_graph_from_point.return_value = mock_graph

        result = self.graph_wrapper.get_graph()
        
        mock_graph_from_point.assert_called_once_with(
            (self.latitude, self.longitude),
            dist=self.map_radius,
            network_type=self.network_type
        )
        self.assertEqual(result, mock_graph)