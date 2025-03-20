from pyflink.datastream.formats.json import JsonRowDeserializationSchema

class JsonRowDeserializationAdapter:
    '''Adapter for serializing and deserializing JSON data'''
    def __init__(self, row_type_config ):
        self.__row_type_info = row_type_config

    def get_deserialization_schema(self):
        return JsonRowDeserializationSchema.builder() \
                .type_info(self.__row_type_info) \
                .build()
