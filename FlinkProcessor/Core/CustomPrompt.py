from string import Template

class CustomPrompt:
    def __init__(self):
        self.__prompt = ""

    def get_prompt(self, user_info_dict, activity_dict):
        activities_list = "\n".join(f" - {activity_name}" for activity_name in activity_dict)
    
        template = Template("""Genera un messaggio pubblicitario personalizzato per attirare l'utente:
                        $user_info

                        La pubblicità deve riguardare una sola attività o nessuna tra quelle elencate. Nella scelta considera 
                        i seguenti criteri in ordine di importanza:
                        1. L'attività deve almeno avere una categoria che corrisponda agli interessi dell'utente.
                        2. Se ci sono più corrispondenze, scegli l'attività più vicina in base a Latitudine e Longitudine.
                        3. Se non c'è corrispondenza, restituisci 'No match'.

                        Queste sono le attività fra cui puoi scegliere:
                        $activities

                        Il messaggio deve essere lungo fra i 200 e 300 caratteri e deve riguardare al massimo una fra le attività. 
                        Il messaggio deve essere uno solo. La risposta deve essere in lingua italiana.""")
    
        self.__prompt = template.substitute(user_info=user_info_dict, activities=activities_list)
        return self.__prompt

   