from Core.IFlinkSerializable import IFlinkSerializable
from pyflink.common import Types
from pyflink.common.types import Row

class MessageElaborated(IFlinkSerializable):
    '''Class to represent the message produced by the map function'''
    def __init__(self,user_id,activity_info,message_id,text,datetime,latitude,longitude):
        self.user_id=user_id
        self.activity_info=activity_info
        self.message_id=message_id
        self.text=text,
        self.datetime=datetime
        self.latitude=latitude
        self.longitude=longitude

    def to_row(self)-> Row:
        '''generates a flink row from the message'''
        row = Row(str(self.user_id),
            str(self.activity_info.activity_id),
            str(self.message_id),
            self.text,
            float(self.activity_info.activity_lat),
            float(self.activity_info.activity_lon),
            self.datetime.strftime("%Y-%m-%d %H:%M:%S"),
            self.latitude,
            self.longitude)
        return row
