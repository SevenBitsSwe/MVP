from abc import ABC, abstractmethod
from pydantic import BaseModel
from Core.PromptTemplate import PromptTemplate
class ILLMService(ABC):
    '''Interface class for the functionalities required from an LLMService'''
    def __init__(self,structured_response: BaseModel,template:PromptTemplate):
        self.__llm_structured_response = structured_response
        self.template=template

    @abstractmethod
    def set_up_chat(self):
        '''initializes the service'''
        pass

    def __get_template(self):#TODO potenzialmente convertire in generazione del promp invece che i figli chiedano il template e generino loro
        '''rethrieves the template used to generate prompts for the llm'''
        return self.template

    @abstractmethod
    def get_llm_structured_response(self,user_info_dict, activity_dict):
        '''allows to generate a message through the service'''
        passTODO