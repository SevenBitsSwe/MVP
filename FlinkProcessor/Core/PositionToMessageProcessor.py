from pyflink.datastream.functions import MapFunction
from Core.LLMService import LLMService
from Core.StructuredResponseMessage import StructuredResponseMessage
from Core.CustomPrompt import CustomPrompt
from pyflink.common.types import Row
from datetime import datetime


class PositionToMessageProcessor(MapFunction):
    '''Map function to transform a position into a message'''
    def __init__(self, ai_chatbot_service: LLMService):
        self.ai_service = ai_chatbot_service
        self.prompt_creator = CustomPrompt()

    def open(self, runtime_context):
        self.__local_chatbot_service = self.ai_service
        pass

    def map(self, value):
        #blablabla
        # user_dict = None # prendi il dict dal db
        # activity_dict = None # prendi il dict dal db
        # current_prompt = self.prompt_creator.get_prompt(user_dict, activity_dict)
        # response_dict = self.__local_chatbot_service.get_llm_structured_response(current_prompt).model_dump()

        row = Row(id=value[0], 
                  message="ciao",
                  latitude=value[2],
                  longitude=value[1],
                  creationTime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        print("wrote message")
        return row