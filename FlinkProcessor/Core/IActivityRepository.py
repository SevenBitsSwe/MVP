from abc import ABC, abstractmethod
from Core.ActivityDTO import ActivityDTO

class IActivityRepository(ABC):
    @abstractmethod
    def get_activity_spec_from_name(self, activity_name) -> ActivityDTO:
        pass

    @abstractmethod
    def get_activities_in_range(self, lon, lat, max_distance) -> list:
        pass
