from pyflink.datastream.functions import FilterFunction
from Core.IMessageRepository import IMessageRepository

class FilterMessageAlreadyDisplayed(FilterFunction):

    def __init__(self,message_repository: IMessageRepository):
        self.__local_repository = message_repository

    def open(self,runtime_context):
        pass

    def filter(self, value):
        coordinates = self.__local_repository.get_user_last_message(value[0])


        if (round(coordinates["latitude"],4) == round(value[4],4) and round(coordinates["longitude"],4) == round(value[5],4)) or value[4] == 0 and value[5]==0:
            print("Filtered")
            return False
        else: 
            return True