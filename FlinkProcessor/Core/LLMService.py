from abc import ABC, abstractmethod
from pydantic import BaseModel

class LLMService(ABC):
    '''Interface class which represent the inbound port, also known as the position receiver'''
    def __init__(self,structured_response: BaseModel):
        self.__llm_structured_response = structured_response

    @abstractmethod
    def set_up_chat(self):
        pass
    
    @abstractmethod
    def get_llm_structured_response(self,prompt):
        pass