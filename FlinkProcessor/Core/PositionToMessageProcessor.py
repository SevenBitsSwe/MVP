from pyflink.datastream.functions import MapFunction
from Core.ILLMService import ILLMService
from Core.StructuredResponseMessage import StructuredResponseMessage
from pyflink.common.types import Row
from datetime import datetime
from Core.ActivityDTO import ActivityDTO
import uuid
from Core.IUserRepository import IUserRepository
from Core.IActivityRepository import IActivityRepository
from Core.MessageElabotated import MessageElaborated

class PositionToMessageProcessor(MapFunction):
    '''Map function to transform a position into a message'''
    def __init__(self, ai_chatbot_service: ILLMService, user_repository: IUserRepository, activity_repository: IActivityRepository):
        self.ai_service = ai_chatbot_service
        self.__user_repository = user_repository
        self.__activity_repository = activity_repository
        self.__NullActivity=ActivityDTO(uuid.uuid4(),"NULL",0,0,"","","")

    def open(self, runtime_context):
        self.ai_service.set_up_chat()
        #self.prompt_creator = CustomPrompt()# gestione del prompt è previsto sia di ILLMService/GroqLLMService

    def map(self, value):
        
        user_dict = self.__user_repository.get_user_who_owns_sensor(str(value[0]))
        activity_dict = self.__activity_repository.get_activities_in_range(value[2], value[1],300)

        if len(activity_dict) == 0:
            message_to_send=MessageElaborated(user_dict.user_uuid,self.__NullActivity,uuid.uuid4(),'skip-this-message',datetime.now(),value[1],value[2])

        ai_response_dict = self.ai_service.get_llm_structured_response(user_dict, activity_dict).model_dump()

        activity_info: ActivityDTO = self.__activity_repository.get_activity_spec_from_name(ai_response_dict['attivita'])
   
        message_to_send=MessageElaborated(user_dict.user_uuid,activity_info,uuid.uuid4(),ai_response_dict['pubblicita'],datetime.now(),value[1],value[2])
        row = message_to_send.to_row()
        print(row)
        return row