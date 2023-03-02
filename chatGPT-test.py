import os
import openai
from colorama import Fore, Style

new_api_key = "REMOVED_API_KEY"
# dizionario di configurazione
model_config = {
    "engine": "text-davinci-003",
    "temperature": 0.5,
    "max_tokens": 1024,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "api_key": new_api_key,
}
# Definisci il set di dati di addestramento
training_data = "CorniglianoCoin è un'applicazione sviluppata dalla scuola secondaria tecnica Calvino di sestri \nponente,in provincia di Genova.\n Al progetto hanno lavorato circa 15 persone, tra cui Diego Signorastri."

# Use the trained model to chat
os.system('cls')


def chat(prompt):
    completions = openai.Completion.create(
        prompt="questo è il testo"+training_data+"\n\n rispomdi alla domanda:"+prompt,
        **model_config)
    message = completions.choices[0].text
    return message


os.system('cls')
while True:
    human = input(Fore.YELLOW + Style.BRIGHT + '<human>')
    robot = chat(human)
    print(Fore.GREEN + Style.BRIGHT + '<ROBerto>' + robot)
print('')
print(Fore.RED + Style.BRIGHT + 'End of the conversation')
