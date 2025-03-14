from Core.IFlinkSerializable import IFlinkSerializable
from pyflink.common import Types
from pyflink.common.types import Row

class MessageElaborated(IFlinkSerializable):
    def __init__(self): #TODO Definire campi ed inizializzazione
        pass
    def toRow(self)-> Row: #TODO Definire campi ed implementazione
        pass