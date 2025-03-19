from Core.ActivityDTO import ActivityDTO
from Core.DatabaseConnection import DatabaseConnection
from typing import List
from abc import ABC, abstractmethod
import uuid

class IActivityRepository(ABC):
    @abstractmethod
    def get_activity_spec_from_name(self, activity_name) -> ActivityDTO:
        pass

    @abstractmethod
    def get_activities_in_range(self, lon, lat, max_distance) -> list:
        pass
