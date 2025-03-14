from abc import ABC, abstractmethod
from pydantic import BaseModel
from Core.PromptTemplate import PromptTemplate
class ILLMService(ABC):
    '''Interface class which represent the inbound port, also known as the position receiver'''
    def __init__(self,structured_response: BaseModel,template:PromptTemplate):
        self.__llm_structured_response = structured_response
        self.template=template

    @abstractmethod
    def set_up_chat(self):
        pass

    def __get_template(self):
        return self.template

    @abstractmethod
    def get_llm_structured_response(self,user_info_dict, activity_dict):
        passTODO