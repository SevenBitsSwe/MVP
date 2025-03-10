import unittest
from unittest.mock import MagicMock, patch, call
from Models.SensorSimulationManager import SensorSimulationManager

class TestSensorSimulationManager(unittest.TestCase):

    def setUp(self):
        self.num_sensors = 10
        self.mock_observer = MagicMock()
        self.mock_strategy = MagicMock()
        self.mock_graph = MagicMock()
        self.mock_graph_instance = MagicMock()
        self.mock_sensor_factory = MagicMock()
        self.mock_graph.get_graph.return_value = self.mock_graph_instance
        
        # Setup mock sensors
        self.mock_sensors = [MagicMock() for _ in range(self.num_sensors)]
        self.mock_sensor_factory.create_gps_sensor.side_effect = self.mock_sensors

    def test_initialization(self):
        """Test correct initialization of SensorSimulationManager"""
            
        manager = SensorSimulationManager(
            self.num_sensors,
            self.mock_observer,
            self.mock_strategy,
            self.mock_graph,
            self.mock_sensor_factory
        )

        self.assertEqual(self.mock_sensor_factory.create_gps_sensor.call_count, self.num_sensors)
        for sensor in self.mock_sensors:
            sensor.register_observer.assert_called_once_with(self.mock_observer)

    @patch('Models.SensorSimulationManager.ThreadPool')
    def test_start_simulation(self, mock_thread_pool):
        """Test che start_simulation crei correttamente il thread pool e avvii la simulazione"""
        # Setup
        mock_pool = MagicMock()
        mock_thread_pool.return_value.__enter__.return_value = mock_pool
            
        manager = SensorSimulationManager(
            self.num_sensors,
            self.mock_observer,
            self.mock_strategy,
            self.mock_graph,
            self.mock_sensor_factory
        )
        
        # Act
        manager.start_simulation()
        
        # Assert
        mock_thread_pool.assert_called_once_with(self.num_sensors)
        mock_pool.map.assert_called_once()
        
        # verify number of sensors passed to call is correct
        args = mock_pool.map.call_args[0]
        self.assertEqual(len(args[1]), self.num_sensors)

    def test_error_handling(self):
        with patch('Models.SensorSimulationManager.ThreadPool') as mock_thread_pool:
            mock_thread_pool.side_effect = Exception("Errore simulato")
            
            manager = SensorSimulationManager(
                self.num_sensors,
                self.mock_observer,
                self.mock_strategy,
                self.mock_graph,
                self.mock_sensor_factory
            )
            
            with self.assertRaises(Exception):
                manager.start_simulation()

