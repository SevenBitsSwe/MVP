from abc import ABC, abstractmethod

class IJsonSerializable(ABC):
    '''Interface class for the JSON serializable class'''
    @abstractmethod
    def serialize_to_json(self):
        '''abstract method to serialize the object to JSON'''
        pass