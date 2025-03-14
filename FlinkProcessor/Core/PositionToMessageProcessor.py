from pyflink.datastream.functions import MapFunction
from Core.ILLMService import ILLMService
from Core.StructuredResponseMessage import StructuredResponseMessage
from pyflink.common.types import Row
from datetime import datetime
from Core.ActivityDTO import ActivityDTO
from Core.MessageDTO import MessageDTO
import uuid
from Core.IUserRepository import IUserRepository
from Core.IActivityRepository import IActivityRepository


class PositionToMessageProcessor(MapFunction):
    '''Map function to transform a position into a message'''
    def __init__(self, ai_chatbot_service: ILLMService, user_repository: IUserRepository, activity_repository: IActivityRepository):
        self.ai_service = ai_chatbot_service
        self.__user_repository = user_repository
        self.__activity_repository = activity_repository

    def open(self, runtime_context):
        self.ai_service.set_up_chat()
        #self.prompt_creator = CustomPrompt()# gestione del prompt è previsto sia di ILLMService/GroqLLMService

    def map(self, value):
        
        user_dict = self.__user_repository.get_user_who_owns_sensor(str(value[0]))
        activity_dict = self.__activity_repository.get_activities_in_range(value[2], value[1],300)

        if len(activity_dict) == 0:
            return Row(str(user_dict.user_uuid),
                        str(uuid.uuid4()),  #non andrebbe un segnaposto che indichi null invece che un casuale?
                        str(uuid.uuid4()),
                        "skip-this-message",
                        0.0,
                        0.0,
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        value[1], #latitude
                        value[2])
        ai_response_dict = self.ai_service.get_llm_structured_response(user_dict, activity_dict).model_dump()

        activity_info: ActivityDTO = self.__activity_repository.get_activity_spec_from_name(ai_response_dict['attivita'])
   
        message_to_send : MessageDTO = MessageDTO(str(user_dict.user_uuid),
                                                  str(activity_info.activity_id),
                                                  str(uuid.uuid4()),
                                                  ai_response_dict['pubblicita'],
                                                  float(activity_info.activity_lat),
                                                  float(activity_info.activity_lon),
                                                  datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                  value[1], #latitude
                                                  value[2]) #longitude

        # row = Row(id=str(user_dict.user_uuid), 
        #           message=ai_response_dict['pubblicita'],
        #           latitude= float(activity_info.activity_lat),
        #           longitude= float(activity_info.activity_lon),
        #           creationTime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        row = Row(str(user_dict.user_uuid),
                                                  str(activity_info.activity_id),
                                                  str(uuid.uuid4()),
                                                  ai_response_dict['pubblicita'],
                                                  float(activity_info.activity_lat),
                                                  float(activity_info.activity_lon),
                                                  datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                  value[1], #latitude
                                                  value[2])
        print(row)
        return row