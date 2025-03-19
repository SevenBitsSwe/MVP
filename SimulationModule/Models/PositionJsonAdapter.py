from Models.IJsonSerializable import IJsonSerializable
from Models.GeoPosition import GeoPosition
import json
class PositionJsonAdapter(IJsonSerializable):
    def serialize_to_json(self, position_istance: GeoPosition):
        '''method to serialize the position to JSON'''

        return json.dumps({
            'user_uuid': position_istance.get_sensor_id(),
            'latitude': float(position_istance.get_latitude()),
            'longitude': float(position_istance.get_longitude()),
            'received_at': position_istance.get_timestamp(),
        })
    
