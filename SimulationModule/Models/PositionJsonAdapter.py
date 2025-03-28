import json
from Models.IJsonSerializable import IJsonSerializable
from Models.GeoPosition import GeoPosition

class PositionJsonAdapter(IJsonSerializable):
    def serialize_to_json(self, object_to_serialize: GeoPosition):
        '''method to serialize the position to JSON'''

        return json.dumps({
            'user_uuid': object_to_serialize.get_sensor_id(),
            'latitude': float(object_to_serialize.get_latitude()),
            'longitude': float(object_to_serialize.get_longitude()),
            'received_at': object_to_serialize.get_timestamp(),
        })
