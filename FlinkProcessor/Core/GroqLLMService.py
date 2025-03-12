from Core.LLMService import LLMService
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

class GroqLLMService(LLMService):
    '''Class that implements the GroqLLMService interface'''
    def __init__(self, structured_response):
        super().__init__(structured_response)
        self.__groq_api_key = os.getenv('PYTHON_PROGRAM_KEY')
        self.__llm_structured_response = structured_response
        self.__chat = self.set_up_chat()

    def set_up_chat(self):
        self.__chat = ChatGroq(
            groq_api_key=self.__groq_api_key,
            model="Gemma2-9b-it",
            temperature=0.6,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            cache=False,
            rate_limiter=InMemoryRateLimiter(
                                            requests_per_second=0.065,  # Quante richieste fare al secondo, in pratica qui posso farne una ogni 10s
                                            check_every_n_seconds=0.1,  # Controlla ogni 100ms (0.1s) se è possibile inviare la richiesta
                                            max_bucket_size=10,  # Dimensione buffer delle richieste
                                            ),
            )
    def get_llm_structured_response(self,prompt ):
        structured_model = self.__chat.with_structured_output(self.__llm_structured_response)
        return structured_model.invoke(prompt)