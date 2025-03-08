import json
from pathlib import Path

class DatabaseConfig:
    def __init__(self):
        self.host = None
        self.port = None
        self.user = None
        self.password = None
    
    @staticmethod
    def load_config():
        config_path = Path(__file__).parent / "config.json"
        with open(config_path) as config_file:
            config = json.load(config_file)
            db_config = DatabaseConfig()
            db_config.host = config['database']['host']
            db_config.database = config['database']['port']
            db_config.user = config['database']['user']
            db_config.password = config['database']['password']
            return db_config