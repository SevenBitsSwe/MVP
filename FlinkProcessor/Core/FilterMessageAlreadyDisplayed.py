from pyflink.datastream.functions import FilterFunction
from Core.IUserRepository import IUserRepository

class FilterMessageAlreadyDisplayed(FilterFunction):

    def __init__(self, user_repository: IUserRepository):
        self.__local_repository = user_repository

    def open(self,runtime_context):
        pass

    def filter(self, value):
        coordinates = self.__local_repository.get_user_last_message_coordinates(value[0])

        
        if (round(coordinates["latitude"],4) == round(value[2],4) and round(coordinates["longitude"],4) == round(value[3],4)) or value[2] == 0 and value[3]==0:
            print("Filtered")
            return False
        else: 
            return True