import os
from random import choice

class F:
    YELLOW = '\033[33m'  
    GREEN = '\033[32m'   
    RED = '\033[31m'     
    RESET = '\033[0m'  
    MAGENTA = '\033[35m'  
    CYAN = '\033[1;36m'
    LIGHT_MAGENTA = '\033[1;95m'

itens = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F',
    'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L',
    'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R',
    's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X',
    'y', 'Y', 'z', 'Z', 
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
    '=', '+', '[', ']', '{', '}', '|', ';', ':', '\'', '"',
    ',', '.', '<', '>', '/', '?', '`', '~'
]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def make_file(text):
    filename = 'p4@ssw0rd.txt'
    try:
        with open(filename, 'r'):
            pass
    except FileNotFoundError:
        with open(filename, 'w') as f:
            f.write('')

    with open(filename, 'a') as file:
        file.write(text)
    return filename

def banner():
    clear()
    print(F.YELLOW+f'''
    ________       __ __            _ 
   / ____/ /      / //_/___ _____  (_)
  / __/ / /      / ,< / __ `/ __ \/ / 
 {F.RED}/ /___/ /___   / /| / /_/ / /_/ / /  
/_____/_____/  /_/ |_\__,_/ .___/_/ {F.LIGHT_MAGENTA}Open Source ++{F.RESET+F.YELLOW}
                         / / 
                        /_/         
'''+F.RESET)

passw = []

banner()
characters = input(F.CYAN + f'[ {F.LIGHT_MAGENTA}!{F.CYAN} ]{F.RESET} Enter the number of characters (Default: {F.CYAN}20{F.RESET} Max: {F.CYAN}93{F.RESET})\n{F.LIGHT_MAGENTA}=>{F.RESET} ').strip()

if len(characters) == 0:
    characters = 20

characters = int(characters)

if characters > 93:
    input(f'\nEnter to exit')
    exit()

for x in range(0, characters):
    while True:
        choiced = choice(itens)
        if choiced not in passw:
            passw.append(choiced)
            break
        else:
            continue # Back to loop

password = ''.join(x for x in passw) # Get The Password

print(F.CYAN+f'\n[ {F.GREEN}✓{F.CYAN} ]{F.RESET} Generated Password: '+password)

while True:
    uname = str(input(F.CYAN + f'\n[ {F.LIGHT_MAGENTA}!{F.CYAN} ]{F.RESET} Enter a name for the password (Remember: {F.CYAN}the name will be used to identify the password in the future{F.RESET}):\n{F.LIGHT_MAGENTA}=>{F.RESET} ').strip().lower())
    if len(uname) < 3:
        continue
    break

file = make_file(uname+' : '+password+'\n')

input(F.CYAN + f'\n[ {F.GREEN}✓{F.CYAN} ]{F.RESET} Password saved successfully: {F.GREEN}{file}{F.RESET} \n\nPress Enter to exit').strip().lower().replace(' ', '')
