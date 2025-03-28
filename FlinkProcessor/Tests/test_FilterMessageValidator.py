import uuid
from datetime import datetime
import unittest
from Core.FilterMessageValidator import FilterMessageValidator

class TestFilterMessageValidator(unittest.TestCase):

    def setUp(self):
        self.validator = FilterMessageValidator()

    def test_valid_message(self):
        """Testa che un messagio valido passi la validazione"""
        valid_message = (
            str(uuid.uuid4()),  # valid UUID
            45.4642,           # valid latitude
            9.1900,            # valid longitude
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # valid timestamp
            "safe content"      # harmless string
        )
        self.assertTrue(self.validator.filter(valid_message))

    def test_invalid_uuid(self):
        """Testa che un UUID non valido fallisca la validazione"""
        invalid_uuid_message = (
            "not-a-uuid",      # invalid UUID
            45.4642,
            9.1900,
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "safe content"
        )
        self.assertFalse(self.validator.filter(invalid_uuid_message))

    def test_invalid_latitude(self):
        """Testa che una latitudine non valida fallisca la validazione"""
        # Latitude out of range
        invalid_lat_message = (
            str(uuid.uuid4()),
            91.0,
            9.1900,
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "safe content"
        )
        self.assertFalse(self.validator.filter(invalid_lat_message))

        # Latitude wrong type
        invalid_lat_type_message = (
            str(uuid.uuid4()),
            "45.4642",
            9.1900,
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "safe content"
        )
        self.assertFalse(self.validator.filter(invalid_lat_type_message))

    def test_invalid_longitude(self):
        """Testa che una longitudine non valida fallisca la validazione"""
        # Longitude out of range
        invalid_lon_message = (
            str(uuid.uuid4()),
            45.4642,
            -181.0,
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "safe content"
        )
        self.assertFalse(self.validator.filter(invalid_lon_message))

        # Longitude wrong type
        invalid_lon_type_message = (
            str(uuid.uuid4()),
            45.4642,
            "9.1900",
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "safe content"
        )
        self.assertFalse(self.validator.filter(invalid_lon_type_message))

    def test_invalid_timestamp(self):
        """Testa che un timestamp non valido fallisca la validazione"""
        invalid_time_message = (
            str(uuid.uuid4()),
            45.4642,
            9.1900,
            "2023-13-01 25:61:61",  # invalid datetime
            "safe content"
        )
        self.assertFalse(self.validator.filter(invalid_time_message))

        # Wrong type
        invalid_time_type_message = (
            str(uuid.uuid4()),
            45.4642,
            9.1900,
            1234567890,         # number instead of string
            "safe content"
        )
        self.assertFalse(self.validator.filter(invalid_time_type_message))

    def test_sql_injection_patterns(self):
        """Testa che un messaggio contenente SQL injection sia rifiutato"""
        sql_injection_messages = [
            (str(uuid.uuid4()), 45.4642, 9.1900, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "SELECT * FROM users"),
            (str(uuid.uuid4()), 45.4642, 9.1900, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DROP TABLE users;"),
            (str(uuid.uuid4()), 45.4642, 9.1900, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "admin' --"),
            (str(uuid.uuid4()), 45.4642, 9.1900, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "UPDATE users SET password='hacked'"),
            (str(uuid.uuid4()), 45.4642, 9.1900, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DELETE FROM users")
        ]
        
        for message in sql_injection_messages:
            self.assertFalse(self.validator.filter(message))

    def test_empty_message(self):
        """Testa che un messaggio vuoto fallisca la validazione"""
        self.assertFalse(self.validator.filter(()))

    def test_partial_message(self):
        """Testa che un messagio incompleto fallisca la validazione"""
        partial_message = (
            str(uuid.uuid4()),
            45.4642
            # missing longitude and timestamp
        )
        self.assertFalse(self.validator.filter(partial_message))

if __name__ == '__main__':
    unittest.main()
