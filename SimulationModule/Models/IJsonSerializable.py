from abc import ABC, abstractmethod

class IJsonSerializable(ABC):
    '''Interface class for the JSON serializable class'''
    @abstractmethod
    def serialize_to_json(self, object_to_serialize: object):
        '''abstract method to serialize the object to JSON'''
        pass
