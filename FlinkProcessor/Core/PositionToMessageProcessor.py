from pyflink.datastream.functions import MapFunction
from Core.LLMService import LLMService
from Core.StructuredResponseMessage import StructuredResponseMessage
from Core.CustomPrompt import CustomPrompt
from pyflink.common.types import Row
from datetime import datetime


from Core.IUserRepository import IUserRepository


class PositionToMessageProcessor(MapFunction):
    '''Map function to transform a position into a message'''
    def __init__(self, ai_chatbot_service: LLMService, user_repository: IUserRepository):
        self.ai_service = ai_chatbot_service
        self.__local_repository = user_repository

    def open(self, runtime_context):
        self.ai_service.set_up_chat()
        self.prompt_creator = CustomPrompt()

    def map(self, value):
        
        user_dict = self.__local_repository.get_user_who_owns_sensor(str(value[0]))
        activity_dict = self.__local_repository.getActivities(value[2], value[1],300)
        print("Coordinates dict: ", activity_dict)
        current_prompt = self.prompt_creator.get_prompt(user_dict, activity_dict)
        ai_response_dict = self.ai_service.get_llm_structured_response(current_prompt).model_dump()

        activity_coordinates = self.__local_repository.getActivityCoordinates(ai_response_dict['attivita'])

        row = Row(id=str(user_dict.user_uuid), 
                  message=ai_response_dict['pubblicita'],
                  latitude= float(activity_coordinates['lat']),
                  longitude= float(activity_coordinates['lon']),
                  creationTime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        print(row)
        return row