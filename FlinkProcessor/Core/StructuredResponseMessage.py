from pydantic import BaseModel, Field

class StructuredResponseMessage(BaseModel):
    '''Class to represent the structured response message'''
    pubblicita: str = Field(descrition="Messaggio pubblicitario prodotto lungo almeno 200 caratteri")
    attivita: str = Field(descrition="Nome della azienda tra quelle proposte di cui è stato prodotto l'annuncio")
