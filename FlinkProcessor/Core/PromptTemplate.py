

class PromptTemplate:
    '''Class to rappresent a template for LLMPromps'''   #sostituisce LLMPrompt/ CustomPrompt Potrebbe essere diviso in interfaccia ed implmntazione specifica
    def __init__(self):
        pass
        #self.__prompt = ""

    def generate_prompt(self,user_info_dict, activity_dict):
        '''generates the prompt to be sent to the llm'''
        prompt = "Genera un messaggio pubblicitario personalizzato per attirare l'utente:\n"
        prompt += str(user_info_dict) + "\n"
        prompt += '''La pubblicità deve riguardare una sola attività o nessuna tra quelle elencate. Nella scelta considera 
                            i seguenti criteri in ordine di importanza:
                            1. L'attività deve almeno avere una categoria che corrisponda agli interessi dell'utente.
                            2. Se ci sono più corrispondenze, scegli l'attività più vicina in base a Latitudine e Longitudine.
                            3. Se non c'è corrispondenza, restituisci 'No match'.'''
        prompt += "\nQueste sono le attività fra cui puoi scegliere:\n"
        for activity_name in activity_dict:
            prompt += " - " + str(activity_name) + "\n"
        prompt += '''Il messaggio deve essere lungo fra i 200 e 300 caratteri e deve riguardare al massimo una fra le attività. 
                     Il messaggio deve essere uno solo. La risposta deve essere in lingua italiana.'''
        return prompt

   