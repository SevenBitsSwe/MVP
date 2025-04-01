from Core.IFlinkSerializable import IFlinkSerializable
from Core.MessageDTO import MessageDTO
from pyflink.common.types import Row

class MessageSerializer(IFlinkSerializable):

    def create_row_from_message(self, message_to_serialize: MessageDTO) -> Row:
        return Row(
            str(message_to_serialize.user_id),
            str(message_to_serialize.activity_id),
            str(message_to_serialize.message_id),
            message_to_serialize.message_text,
            message_to_serialize.activity_lat,
            message_to_serialize.activity_lon,
            str(message_to_serialize.creation_time),
            message_to_serialize.user_lat,
            message_to_serialize.user_lon
        )
