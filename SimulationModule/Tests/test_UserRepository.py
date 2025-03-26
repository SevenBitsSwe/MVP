import uuid
import unittest
from unittest.mock import Mock
from Models.UserRepository import UserRepository
from Models.DatabaseConnection import DatabaseConnection
from Models.UserDTO import UserDTO

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.mock_db_connection = Mock(spec=DatabaseConnection)

        self.user_repository = UserRepository(self.mock_db_connection)

    def test_mark_user_as_occupied(self):
        mock_conn = Mock()
        self.mock_db_connection.connect.return_value = mock_conn

        test_user_uuid = uuid.uuid4()
        test_sensor_uuid = uuid.uuid4()

        self.user_repository.mark_user_as_occupied(test_user_uuid,test_sensor_uuid)

        self.mock_db_connection.connect.assert_called_once()
        self.mock_db_connection.disconnect.assert_called_once()

        expected_query = f"ALTER TABLE nearyou.user UPDATE assigned_sensor_uuid = '{test_sensor_uuid}' WHERE user_uuid = '{test_user_uuid}'"
        mock_conn.query.assert_called_once_with(expected_query)

    def test_get_free_user(self):
        mock_conn = Mock()
        self.mock_db_connection.connect.return_value = mock_conn

        test_user_uuid = uuid.uuid4()
        test_name = "John"
        test_surname = "Doe"
        test_email = "john.doe@example.com"
        test_gender = "Male"
        test_birthdate = "1990-01-01"
        test_civil_status = "Single"
        mock_conn.query.return_value.result_rows = [
            (test_user_uuid, None, test_name, test_surname, test_email, test_gender, test_birthdate, test_civil_status)
        ]

        result = self.user_repository.get_free_user()

        self.mock_db_connection.connect.assert_called_once()
        self.mock_db_connection.disconnect.assert_called_once()

        expected_query = "SELECT user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status FROM nearyou.user WHERE assigned_sensor_uuid IS NULL"
        mock_conn.query.assert_called_once_with(expected_query)

        self.assertIsInstance(result, UserDTO)
        self.assertEqual(result.user_uuid, test_user_uuid)
        self.assertIsNone(result.assigned_sensor_uuid)
        self.assertEqual(result.name, test_name)
        self.assertEqual(result.surname, test_surname)
        self.assertEqual(result.email, test_email)
        self.assertEqual(result.gender, test_gender)
        self.assertEqual(result.birthdate, test_birthdate)
        self.assertEqual(result.civil_status, test_civil_status)

    def test_get_free_user_no_result(self):
        mock_conn = Mock()
        self.mock_db_connection.connect.return_value = mock_conn
        mock_conn.query.return_value.result_rows = []

        result = self.user_repository.get_free_user()

        self.mock_db_connection.connect.assert_called_once()
        self.mock_db_connection.disconnect.assert_called_once()

        expected_query = "SELECT user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status FROM nearyou.user WHERE assigned_sensor_uuid IS NULL"
        mock_conn.query.assert_called_once_with(expected_query)

        self.assertIsNone(result)
