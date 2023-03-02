import os
import openai
from colorama import Fore, Style

new_api_key = "REMOVED_API_KEY"

prompts = [
    "Domanda: Come mi chiamo?\nRisposta: Tu ti chiami Diego.",
    "Domanda: Qual è il mio nome?\nRisposta: Il tuo nome è Diego.",
    "Domanda: Mi puoi dire il mio nome?\nRisposta: Certamente, tu ti chiami Diego."
]


# Use the trained model to chat
os.system('cls')
def chat(prompt):
    completions = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=1024,
                                           api_key=new_api_key)
    message = completions.choices[0].text
    return message


os.system('cls')
i = 1
while i < 6:
    human = input(Fore.YELLOW + Style.BRIGHT+'<human>')
    robot = chat(human)
    print(Fore.GREEN + Style.BRIGHT + '<ROBerto>' + robot)
    i = i + 1
print('')
print(Fore.RED + Style.BRIGHT + 'End of the conversation')
