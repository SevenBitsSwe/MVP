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
        
        # Configura il sensore mock
        self.sensor_uuid = uuid.uuid4()
        self.mock_sensor.get_sensor_uuid.return_value = self.sensor_uuid
        
        # Configura il grafo mock
        self.mock_graph = MagicMock()
        self.mock_graph.nodes = {
            1: {"y": 45.0, "x": 9.0},
            2: {"y": 45.1, "x": 9.1}
        }

    def test_initialization(self):
        """Verifica che il costruttore inizializzi correttamente i valori predefiniti"""
        # Verifica i valori privati attraverso l'accesso diretto (in un contesto di test è accettabile)
        self.assertEqual(self.strategy._BycicleSimulationStrategy__bycicle_speed_approximated, 15)
        self.assertEqual(self.strategy._BycicleSimulationStrategy__delta_time_between_positions, 10)
    
    @patch('random.choice')
    @patch('osmnx.shortest_path')
    @patch('time.sleep')  # Per evitare ritardi nei test
    @patch('datetime.datetime')
    def test_simulate_position_live_update_basic(self, mock_datetime, mock_sleep, mock_shortest_path, mock_choice):
        """Test del comportamento di base del metodo simulate_position_live_update"""
        # Configura mock per random.choice
        mock_choice.side_effect = [1, 2]
        
        # Configura mock per datetime.now
        mock_now = MagicMock()
        mock_now.strftime.return_value = "2023-01-01 12:00:00"
        mock_datetime.now.return_value = mock_now
        
        # Configura mock per shortest_path
        mock_shortest_path.return_value = [1, 2]
        
        # Patcha geodesic per restituire una distanza controllata
        with patch('geopy.distance.geodesic') as mock_geodesic:
            mock_distance = MagicMock()
            mock_distance.meters = 1000  # 1 km tra i punti
            mock_geodesic.return_value = mock_distance
            
            # Esegue il metodo da testare
            self.strategy.simulate_position_live_update(self.mock_sensor, self.mock_graph)
            
            # Verifica le chiamate ai mock
            mock_choice.assert_called()
            mock_shortest_path.assert_called_once_with(
                self.mock_graph,
                1,
                2,
                weight='length'
            )
            
            # Verifica che set_current_position sia stato chiamato almeno una volta
            self.mock_sensor.set_current_position.assert_called()
            
            # Verifica che time.sleep sia stato chiamato
            mock_sleep.assert_called()
    
        # Modifica questo decoratore per puntare al percorso esatto di datetime
    @patch('Models.BycicleSimulationStrategy.datetime')
    @patch('random.choice', side_effect=[1, 2])
    @patch('osmnx.shortest_path', return_value=[1, 2])
    @patch('time.sleep')  # Per evitare ritardi nei test
    def test_position_update_correct_parameters(self, mock_sleep, mock_shortest_path, mock_choice, mock_datetime):
        """Verifica che la posizione del sensore venga aggiornata con i parametri corretti"""
        # Configura datetime.now
        mock_now = MagicMock()
        mock_now.strftime.return_value = "2023-01-01 12:00:00"
        mock_datetime.now.return_value = mock_now
        
        # Patcha geodesic
        with patch('geopy.distance.geodesic') as mock_geodesic:
            mock_distance = MagicMock()
            mock_distance.meters = 1000
            mock_geodesic.return_value = mock_distance
            
            # Esegue il metodo
            self.strategy.simulate_position_live_update(self.mock_sensor, self.mock_graph)
            
            # Estrae l'argomento passato a set_current_position
            args, _ = self.mock_sensor.set_current_position.call_args
            position = args[0]
            
            # Verifica l'oggetto GeoPosition
            self.assertIsInstance(position, GeoPosition)
            self.assertEqual(position.get_sensor_id(), str(self.sensor_uuid))
            self.assertEqual(position.get_timestamp(), "2023-01-01 12:00:00")
            
            # Le coordinate sono calcolate dinamicamente quindi verifichiamo il tipo
            self.assertIsInstance(position.get_latitude(), float)
            self.assertIsInstance(position.get_longitude(), float)