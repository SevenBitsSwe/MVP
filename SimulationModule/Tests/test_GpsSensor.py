import unittest
from unittest.mock import MagicMock, patch
import uuid
from Models.GeoPosition import GeoPosition
from Models.GpsSensor import GpsSensor
from Models.PositionSender import PositionSender
from Models.IPositionSimulationStrategy import IPositionSimulationStrategy

class TestGpsSensor(unittest.TestCase):
    def setUp(self):
        #PositionSender and IPositionSimulationStrategy mock
        self.mock_position_sender = MagicMock(spec=PositionSender)
        self.mock_simulation_strategy = MagicMock(spec=IPositionSimulationStrategy)
        
        #IPositionSimulationStrategy mock
        self.mock_simulation_strategy.get_speed.return_value = 4.1667
        self.mock_simulation_strategy.get_route.return_value = [(45.0, 9.0), (45.1, 9.1)]
        
        # Inizializziamo il sensore GPS con i mock
        self.test_uuid = uuid.uuid4()
        self.test_sensor = GpsSensor(self.test_uuid, self.mock_position_sender, self.mock_simulation_strategy)
    
    def test_initialization(self):
        """Verifica che il costruttore inizializzi correttamente i valori"""
        self.assertEqual(self.test_sensor._sensor_uuid, self.test_uuid)
        self.assertEqual(self.test_sensor._GpsSensor__position_sender, self.mock_position_sender)
        self.assertEqual(self.test_sensor._GpsSensor__speed_mps, 4.1667)

    @patch('time.sleep', return_value=None)
    @patch('geopy.distance.geodesic')
    def test_simulate(self, mock_geodesic, mock_sleep):
        """Test del metodo simulate per verificare che invii correttamente le posizioni"""
        # geodesic mock
        mock_distance = MagicMock()
        mock_distance.meters = 1000  # 1 km tra i punti
        mock_geodesic.return_value = mock_distance
        
        self.test_sensor.simulate()
        
        self.mock_simulation_strategy.get_route.assert_called_once()
        self.mock_position_sender.send_position.assert_called()
        mock_sleep.assert_called()

    @patch('Models.GpsSensor.datetime')
    def test_create_geo_position(self, mock_datetime):
        mock_now = MagicMock()
        mock_now.strftime.return_value = "2023-01-01 12:00:00"
        mock_datetime.now.return_value = mock_now
        
        latitude = 45.0
        longitude = 9.0
        position = self.test_sensor.create_geo_position(latitude, longitude)
        self.assertIsInstance(position, GeoPosition)
        self.assertEqual(position.get_sensor_id(), str(self.test_uuid))
        self.assertEqual(position.get_latitude(), latitude)
        self.assertEqual(position.get_longitude(), longitude)
        self.assertEqual(position.get_timestamp(), "2023-01-01 12:00:00")

    def test_get_sensor_uuid(self):
        """Verifica che il metodo get_sensor_uuid restituisca l'UUID corretto"""
        self.assertEqual(self.test_sensor.get_sensor_uuid(), self.test_uuid)

    def test_get_update_time(self):
        """Verifica che il metodo get_update_time restituisca il tempo di aggiornamento della SimulationStrategy assegnata"""
        expected_update_time = 20
        self.mock_simulation_strategy.get_delta_time.return_value = expected_update_time
        self.assertEqual(self.test_sensor.get_update_time(), expected_update_time)
