from pyflink.datastream.functions import MapFunction

class PositionToMessageProcessor(MapFunction):
    '''Map function to transform a position into a message'''
    def open(self, runtime_context):
        pass
    
    def map(self, value):
        return value