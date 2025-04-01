import unittest
import uuid
from datetime import datetime
from Core.MessageDTO import MessageDTO
from Core.UserDTO import UserDTO
from Core.ActivityDTO import ActivityDTO

class TestDataTransferObjects(unittest.TestCase):
    """Test suite for Data Transfer Objects used in the application."""

    def test_message_dto_initialization(self):
        """Test that MessageDTO correctly initializes with provided values."""
        # Create a MessageDTO with specific values
        user_id = uuid.uuid4()
        activity_id = uuid.uuid4()
        message_id = uuid.uuid4()
        message_text = "Test message"
        activity_lat = 45.4642
        activity_lon = 9.1900
        creation_time = datetime.now()
        user_lat = 45.4646
        user_lon = 9.1904

        message = MessageDTO(
            user_id=user_id,
            activity_id=activity_id,
            message_id=message_id,
            message_text=message_text,
            activity_lat=activity_lat,
            activity_lon=activity_lon,
            creation_time=creation_time,
            user_lat=user_lat,
            user_lon=user_lon
        )

        # Verify all values are correctly stored
        self.assertEqual(message.user_id, str(user_id))
        self.assertEqual(message.activity_id, str(activity_id))
        self.assertEqual(message.message_id, str(message_id))
        self.assertEqual(message.message_text, message_text)
        self.assertEqual(message.activity_lat, activity_lat)
        self.assertEqual(message.activity_lon, activity_lon)
        self.assertEqual(message.creation_time, creation_time)
        self.assertEqual(message.user_lat, user_lat)
        self.assertEqual(message.user_lon, user_lon)

    def test_message_dto_default_values(self):
        """Test that MessageDTO correctly sets default values when not provided."""
        # Create a MessageDTO with default values
        message = MessageDTO()

        # Verify UUIDs are generated and other defaults are set
        self.assertTrue(isinstance(uuid.UUID(message.user_id), uuid.UUID))
        self.assertTrue(isinstance(uuid.UUID(message.activity_id), uuid.UUID))
        self.assertTrue(isinstance(uuid.UUID(message.message_id), uuid.UUID))
        self.assertEqual(message.message_text, "")
        self.assertEqual(message.activity_lat, 0.0)
        self.assertEqual(message.activity_lon, 0.0)
        self.assertEqual(message.creation_time, "")
        self.assertEqual(message.user_lat, 0.0)
        self.assertEqual(message.user_lon, 0.0)

    def test_user_initialization(self):
        """Test that UserDTO correctly initializes with provided values."""
        # Create test data
        user_uuid = uuid.uuid4()
        assigned_sensor_uuid = uuid.uuid4()
        name = "John"
        surname = "Doe"
        email = "john.doe@example.com"
        gender = "Male"
        birthdate = "1990-01-01"
        civil_status = "Single"
        interests = ["Sports", "Reading", "Music"]

        # Create a UserDTO with the test data
        user = UserDTO(
            user_uuid=user_uuid,
            assigned_sensor_uuid=assigned_sensor_uuid,
            name=name,
            surname=surname,
            email=email,
            gender=gender,
            birthdate=birthdate,
            civil_status=civil_status,
            interests=interests
        )

        # Verify all values are correctly stored
        self.assertEqual(user.user_uuid, user_uuid)
        self.assertEqual(user.assigned_sensor_uuid, assigned_sensor_uuid)
        self.assertEqual(user.name, name)
        self.assertEqual(user.surname, surname)
        self.assertEqual(user.email, email)
        self.assertEqual(user.gender, gender)
        self.assertEqual(user.birthdate, birthdate)
        self.assertEqual(user.civil_status, civil_status)
        self.assertEqual(user.interests, interests)

    def test_user_with_default_interests(self):
        """Test that UserDTO correctly handles the default value for interests."""
        # Create a UserDTO without specifying interests
        user_uuid = uuid.uuid4()
        assigned_sensor_uuid = uuid.uuid4()

        user = UserDTO(
            user_uuid=user_uuid,
            assigned_sensor_uuid=assigned_sensor_uuid,
            name="Jane",
            surname="Smith",
            email="jane.smith@example.com",
            gender="Female",
            birthdate="1992-05-15",
            civil_status="Married"
        )

        # Verify that interests is None when not provided
        self.assertIsNone(user.interests)

    def test_user_with_empty_interests(self):
        """Test that UserDTO correctly handles empty interests list."""
        # Create a UserDTO with empty interests list
        user_uuid = uuid.uuid4()
        assigned_sensor_uuid = uuid.uuid4()

        user = UserDTO(
            user_uuid=user_uuid,
            assigned_sensor_uuid=assigned_sensor_uuid,
            name="Alex",
            surname="Brown",
            email="alex.brown@example.com",
            gender="Non-binary",
            birthdate="1988-11-23",
            civil_status="Divorced",
            interests=[]
        )

        # Verify that interests is an empty list
        self.assertEqual(user.interests, [])
        self.assertIsInstance(user.interests, list)

    def test_activity_initialization(self):
        """Test that ActivityDTO correctly initializes with provided values."""
        # Create an ActivityDTO with specific values
        activity_id = uuid.uuid4()
        activity_name = "Mountain Hike"
        activity_lon = 9.1900
        activity_lat = 45.4642
        activity_addr = "Mountain Park, Alps"
        activity_type = "Outdoor"
        activity_description = "A beautiful hiking trail"

        activity = ActivityDTO(
            activity_id=activity_id,
            activity_name=activity_name,
            activity_lon=activity_lon,
            activity_lat=activity_lat,
            activity_addr=activity_addr,
            activity_type=activity_type,
            activity_description=activity_description
        )

        # Verify all values are correctly stored
        self.assertEqual(activity.activity_id, activity_id)  # Note: ActivityDTO doesn't convert UUID to string
        self.assertEqual(activity.activity_name, activity_name)
        self.assertEqual(activity.activity_lon, activity_lon)
        self.assertEqual(activity.activity_lat, activity_lat)
        self.assertEqual(activity.activity_addr, activity_addr)
        self.assertEqual(activity.activity_type, activity_type)
        self.assertEqual(activity.activity_description, activity_description)

    def test_activity_default_values(self):
        """Test that ActivityDTO correctly sets default values when not provided."""
        # Create an ActivityDTO with default values
        activity = ActivityDTO()

        # Verify defaults are set
        self.assertTrue(isinstance(activity.activity_id, uuid.UUID))
        self.assertEqual(activity.activity_name, "")
        self.assertEqual(activity.activity_lon, 0.0)
        self.assertEqual(activity.activity_lat, 0.0)
        self.assertEqual(activity.activity_addr, "")
        self.assertEqual(activity.activity_type, "")
        self.assertEqual(activity.activity_description, "")

    def test_activity_partial_initialization(self):
        """Test initialization with only some parameters specified."""
        # Create an ActivityDTO with only some values
        activity = ActivityDTO(
            activity_name="Beach Day",
            activity_lat=41.1234
        )

        # Verify specified values are set
        self.assertEqual(activity.activity_name, "Beach Day")
        self.assertEqual(activity.activity_lat, 41.1234)

        # Verify unspecified values get defaults
        self.assertTrue(isinstance(activity.activity_id, uuid.UUID))
        self.assertEqual(activity.activity_lon, 0.0)
        self.assertEqual(activity.activity_addr, "")
        self.assertEqual(activity.activity_type, "")
        self.assertEqual(activity.activity_description, "")
