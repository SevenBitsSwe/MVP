import unittest
from unittest.mock import MagicMock,patch
import uuid
from Models.GpsSensor import GpsSensor
from Models.BycicleSimulationStrategy import BycicleSimulationStrategy
from Models.GraphWrapper import GraphWrapper

class TestBycicleSimulationStrategy(unittest.TestCase):

    def setUp(self):
        # graph mock
        self.mock_graph_wrapper = MagicMock(spec=GraphWrapper)
        self.mock_graph = MagicMock()
        self.mock_graph.nodes = {
            1: {"y": 45.0, "x": 9.0},
            2: {"y": 45.1, "x": 9.1}
        }
        self.mock_graph_wrapper.get_graph.return_value = self.mock_graph

        self.strategy = BycicleSimulationStrategy(self.mock_graph_wrapper)
        self.mock_sensor = MagicMock(spec=GpsSensor)

        # sensor mock
        self.sensor_uuid = uuid.uuid4()
        self.mock_sensor.get_sensor_uuid.return_value = self.sensor_uuid

    def test_initialization(self):
        """Verifica che il costruttore inizializzi correttamente i valori predefiniti"""
        # verify private values
        self.assertEqual(self.strategy._BycicleSimulationStrategy__bycicle_speed_approximated, 15)
        self.assertEqual(self.strategy._BycicleSimulationStrategy__delta_time_between_positions, 21)
        self.assertEqual(self.strategy._BycicleSimulationStrategy__graph_istance, self.mock_graph)

    @patch('random.choice')
    @patch('osmnx.shortest_path')
    def test_get_route(self, mock_shortest_path, mock_choice):
        """Test del comportamento di base del metodo simulate_position_live_update"""
        # mock random choice
        mock_choice.side_effect = [1, 2]

        # configure mock
        mock_shortest_path.return_value = [1, 2]

        route_coords = self.strategy.get_route()

        # verify mock calls
        mock_choice.assert_called()
        mock_shortest_path.assert_called_once_with(
            self.mock_graph,
            1,
            2,
            weight='length'
        )

        # verify that the coordinates are corrects
        expected_coords = [(45.0, 9.0), (45.1, 9.1)]
        self.assertEqual(route_coords, expected_coords)

    def test_get_delta_time(self):
        """Verifica che il metodo get_delta_time restituisca il valore corretto"""
        delta_time = self.strategy.get_delta_time()
        self.assertEqual(delta_time, 21)

    def test_get_speed(self):
        """Verifica che il metodo get_speed restituisca il valore corretto"""
        speed = self.strategy.get_speed()
        expected_speed = 15 / 3.6
        self.assertEqual(speed, expected_speed)
