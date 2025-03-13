

class CustomPrompt:
    def __init__(self):
        self.__prompt = ""

    def get_prompt(self, user_info_dict, activity_dict):
        self.__prompt = "Genera un messaggio pubblicitario personalizzato per attirare l'utente:\n"
        self.__prompt += str(user_info_dict) + "\n"
        self.__prompt += '''La pubblicità deve riguardare una sola attività o nessuna tra quelle elencate. Nella scelta considera 
                            i seguenti criteri in ordine di importanza:
                            1. L'attività deve almeno avere una categoria che corrisponda agli interessi dell'utente.
                            2. Se ci sono più corrispondenze, scegli l'attività più vicina in base a Latitudine e Longitudine.
                            3. Se non c'è corrispondenza, restituisci 'No match'.'''
        self.__prompt += "\nQueste sono le attività fra cui puoi scegliere:\n"
        for activity_name in activity_dict:
            self.__prompt += " - " + str(activity_name) + "\n"
        self.__prompt += '''Il messaggio deve essere lungo fra i 200 e 300 caratteri e deve riguardare al massimo una fra le attività. 
                     Il messaggio deve essere uno solo. La risposta deve essere in lingua italiana.'''
        return self.__prompt

   