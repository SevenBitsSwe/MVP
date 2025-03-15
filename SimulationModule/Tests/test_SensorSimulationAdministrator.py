import unittest
from unittest.mock import MagicMock, patch
from Models.SensorSimulationAdministrator import SensorSimulationAdministrator

class TestSensorSimulationAdministrator(unittest.TestCase):

    def setUp(self):
        self.num_sensors = 10
        self.mock_sensors = [MagicMock() for _ in range(self.num_sensors)]

    def test_initialization(self):
        """Test correct initialization of SensorSimulationManager"""
            
        manager = SensorSimulationAdministrator(self.mock_sensors)

        self.assertEqual(manager._SensorSimulationAdministrator__sensor_registry, self.mock_sensors)

    @patch('Models.SensorSimulationAdministrator.ThreadPool')
    def test_start_simulation(self, mock_thread_pool):
        """Test che start_simulation crei correttamente il thread pool e avvii la simulazione"""
        # Setup
        mock_pool = MagicMock()
        mock_thread_pool.return_value.__enter__.return_value = mock_pool
            
        manager = SensorSimulationAdministrator(self.mock_sensors)
        
        # Act
        manager.start_simulation()
        
        # Assert
        mock_thread_pool.assert_called_once_with(self.num_sensors)
        mock_pool.map.assert_called_once()
        
        # verify number of sensors passed to call is correct
        args = mock_pool.map.call_args[0]
        self.assertEqual(args[0].__name__, "<lambda>")
        self.assertEqual(args[1], self.mock_sensors)

    def test_error_handling(self):
        with patch('Models.SensorSimulationAdministrator.ThreadPool') as mock_thread_pool:
            mock_thread_pool.side_effect = Exception("Errore simulato")
            
            manager = SensorSimulationAdministrator(self.mock_sensors)
            
            with self.assertRaises(Exception):
                manager.start_simulation()

