from pyflink.datastream.formats.json import JsonRowSerializationSchema

class JsonRowSerializationAdapter:
    '''Adapter for serializing and deserializing JSON data'''
    def __init__(self, row_type_config_message ):
        self.__row_type_info_message = row_type_config_message

    def get_serialization_schema(self):
        return JsonRowSerializationSchema.builder()\
                                         .with_type_info(self.__row_type_info_message)\
                                         .build()
