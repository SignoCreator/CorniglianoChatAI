import os
import openai
from colorama import Fore, Style

new_api_key = "REMOVED_API_KEY"


def chat(prompt):
    completions = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=1024,
                                           api_key=new_api_key)
    message = completions[0].text
    return message


os.system('cls')
i = 1
while i < 6:
    human = input(Fore.YELLOW + Style.BRIGHT)
    robot = chat(human)
    print(Fore.GREEN + Style.BRIGHT + '<little robot>' + robot)
    i = i + 1
print('')
print(Fore.RED + Style.BRIGHT + 'End of the conversation')
