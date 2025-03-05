import unittest
from unittest.mock import MagicMock, patch, call

# Rimuovi questo import
# import functools
# from multiprocessing.pool import ThreadPool

from Models.SensorSimulationManager import SensorSimulationManager
from Models.SensorFactory import SensorFactory
from Models.IPositionObserver import IPositionObserver
from Models.IPositionSimulationStrategy import IPositionSimulationStrategy

class TestSensorSimulationManager(unittest.TestCase):

    def setUp(self):
        # Crea i mock per le dipendenze
        self.mock_observer = MagicMock(spec=IPositionObserver)
        self.mock_strategy = MagicMock(spec=IPositionSimulationStrategy)
        self.mock_graph = MagicMock()
        self.mock_graph_object = MagicMock()
        self.mock_graph.get_graph.return_value = self.mock_graph_object
        
        # Configura il numero di sensori per i test
        self.num_sensors = 3
        
        # Mock per i sensori
        self.mock_sensors = []
        for i in range(self.num_sensors):
            mock_sensor = MagicMock()
            mock_sensor.register_observer = MagicMock()
            self.mock_sensors.append(mock_sensor)
    
    