from Models.IPositionSimulationStrategy import IPositionSimulationStrategy
from Models.GpsSensor import GpsSensor
from Models.GeoPosition import GeoPosition
from Models.BycicleSimulationStrategy import BycicleSimulationStrategy
from Models.GraphWrapper import GraphWrapper
import unittest 
from unittest.mock import MagicMock,patch
from datetime import datetime
from geopy.distance import geodesic
import uuid

class TestBycicleSimulationStrategy(unittest.TestCase):
    
    def setUp(self):
        self.strategy = BycicleSimulationStrategy()
        self.mock_sensor = MagicMock(spec=GpsSensor)
        
        # sensor mock
        self.sensor_uuid = uuid.uuid4()
        self.mock_sensor.get_sensor_uuid.return_value = self.sensor_uuid
        
        # graph mock
        self.mock_graph = MagicMock()
        self.mock_graph.nodes = {
            1: {"y": 45.0, "x": 9.0},
            2: {"y": 45.1, "x": 9.1}
        }

    def test_initialization(self):
        """Verifica che il costruttore inizializzi correttamente i valori predefiniti"""
        # verify private values
        self.assertEqual(self.strategy._BycicleSimulationStrategy__bycicle_speed_approximated, 15)
        self.assertEqual(self.strategy._BycicleSimulationStrategy__delta_time_between_positions, 20)
    
    @patch('random.choice')
    @patch('osmnx.shortest_path')
    @patch('time.sleep') 
    @patch('datetime.datetime')
    def test_simulate_position_live_update_basic(self, mock_datetime, mock_sleep, mock_shortest_path, mock_choice):
        """Test del comportamento di base del metodo simulate_position_live_update"""
        # mock random choice
        mock_choice.side_effect = [1, 2]
        
        # mock for datetime
        mock_now = MagicMock()
        mock_now.strftime.return_value = "2023-01-01 12:00:00"
        mock_datetime.now.return_value = mock_now
        
        # configure mock
        mock_shortest_path.return_value = [1, 2]
        
        # patch geodesic
        with patch('geopy.distance.geodesic') as mock_geodesic:
            mock_distance = MagicMock()
            mock_distance.meters = 1000  # 1 km tra i punti
            mock_geodesic.return_value = mock_distance
            
            # method to test
            self.strategy.simulate_position_live_update(self.mock_sensor, self.mock_graph)
            
            # verify mock calls
            mock_choice.assert_called()
            mock_shortest_path.assert_called_once_with(
                self.mock_graph,
                1,
                2,
                weight='length'
            )
            
            # verify set current position called at least one time
            self.mock_sensor.set_current_position.assert_called()
            
            # verify sleep called at least one time
            mock_sleep.assert_called()
    
    
    @patch('Models.BycicleSimulationStrategy.datetime')
    @patch('random.choice', side_effect=[1, 2])
    @patch('osmnx.shortest_path', return_value=[1, 2])
    @patch('time.sleep') 
    def test_position_update_correct_parameters(self, mock_sleep, mock_shortest_path, mock_choice, mock_datetime):
        """Verifica che la posizione del sensore venga aggiornata con i parametri corretti"""
        
        mock_now = MagicMock()
        mock_now.strftime.return_value = "2023-01-01 12:00:00"
        mock_datetime.now.return_value = mock_now
        
        
        with patch('geopy.distance.geodesic') as mock_geodesic:
            mock_distance = MagicMock()
            mock_distance.meters = 1000
            mock_geodesic.return_value = mock_distance
            
           
            self.strategy.simulate_position_live_update(self.mock_sensor, self.mock_graph)
            
            # extract arguments passed to set_current_position
            args, _ = self.mock_sensor.set_current_position.call_args
            position = args[0]
            
            # verify geoposition object
            self.assertIsInstance(position, GeoPosition)
            self.assertEqual(position.get_sensor_id(), str(self.sensor_uuid))
            self.assertEqual(position.get_timestamp(), "2023-01-01 12:00:00")
            
            # verify coordinates type
            self.assertIsInstance(position.get_latitude(), float)
            self.assertIsInstance(position.get_longitude(), float)