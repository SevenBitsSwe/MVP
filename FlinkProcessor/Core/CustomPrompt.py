from string import Template

class CustomPrompt:
    def __init__(self):
        self.__template = Template("""Genera un messaggio pubblicitario personalizzato per attirare l'utente:
                        $user_info

                        Per questa attività:
                        $activity

                        Il messaggio deve essere lungo fra i 200 e 300 caratteri e deve riguardare al massimo una fra le attività. 
                        Il messaggio deve essere uno solo. La risposta deve essere in lingua italiana.""")

    def get_prompt(self, user_info_dict, activity):

        prompt = self.__template.substitute(user_info=user_info_dict, activity=activity)
        return prompt
