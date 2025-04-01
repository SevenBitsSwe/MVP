import uuid
from datetime import datetime
import unittest
from Core.FilterMessageValidator import FilterMessageValidator

class TestFilterMessageValidator(unittest.TestCase):

    def setUp(self):
        self.validator = FilterMessageValidator()

    def test_valid_message(self):
        """Test that a valid message passes validation"""
        valid_message = (
            str(uuid.uuid4()),  # valid UUID
            45.4642,           # valid latitude
            9.1900,            # valid longitude
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # valid timestamp
            "safe content"      # harmless string
        )
        self.assertTrue(self.validator.filter(valid_message))

    def test_invalid_uuid(self):
        """Test that an invalid UUID fails validation"""
        invalid_uuid_message = (
            "not-a-uuid",      # invalid UUID
            45.4642,
            9.1900,
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "safe content"
        )
        self.assertFalse(self.validator.filter(invalid_uuid_message))

    def test_invalid_latitude(self):
        """Test that an invalid latitude fails validation"""
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
        """Test that an invalid longitude fails validation"""
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
        """Test that an invalid timestamp fails validation"""
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
        """Test whether a message containing SQL injection is rejected"""
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
        """Test that an empty message fails validation"""
        self.assertFalse(self.validator.filter(()))

    def test_partial_message(self):
        """Test that an incomplete message fails validation"""
        partial_message = (
            str(uuid.uuid4()),
            45.4642
            # missing longitude and timestamp
        )
        self.assertFalse(self.validator.filter(partial_message))

if __name__ == '__main__':
    unittest.main()
