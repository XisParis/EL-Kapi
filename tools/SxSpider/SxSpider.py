from bs4 import BeautifulSoup as bs4
import requests, os 

class F:
    YELLOW = '\033[33m'  
    GREEN = '\033[32m'   
    RED = '\033[31m'     
    RESET = '\033[0m'  
    MAGENTA = '\033[35m'  

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    clear()
    print(F.GREEN+f'''   ______  __    _____ ____  ________  ____________
  / ___/ |/ /   / ___// __ \/  _/ __ \/ ____/ __  /
  \__ \|   /    \__ \/ /_/ // // / / / __/ / /_/ /
 ___/ /   |    ___/ / ____// // /_/ / /___/ _, _/ 
/____/_/|_|   /____/_/   /___/_____/_____/_/ |_| 
            {F.MAGENTA}Open Source Tool ( {F.GREEN}Modifications Allowed 🎲{F.MAGENTA} ){F.GREEN}
            ''', F.RESET)

def filter_url(link):
    if '=http' in link:
        print(F.GREEN+f'< OPEN REDIRECT WARNING > {F.RESET+link}')
    elif '?' in link:
        print(F.YELLOW+f'< PARAMETER > {F.RESET+link}')
    else:
        print(F.RED+f'< URL > {F.RESET+link}')

def save_a_link(link):
    with open('Links.txt', 'a') as file:
        file.write(link+'\n')

def make_file(filename):
    with open(filename, 'w') as file:  
        file.write('')     
            
banner()

url = str(input(f'[ {F.GREEN}?{F.RESET} ] Url/Domain: \n➤  ')).strip().lower()

if not url.startswith('http'):
    url = 'http://'+url

if url.endswith('/'):
    url = url[0:len(url)-1] # Remove '/' 

domain = url.split('://')[1]
protocoloHTTP = url.split('://')[0] # Not in use

print(f'[ {F.MAGENTA}#{F.RESET} ] Searching... [ TARGET: {F.YELLOW+domain+F.RESET} ]\n')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

try:
    re = requests.get(url, headers=headers)
except requests.exceptions.ConnectionError:
    print(F.RED+'Invalid Website')
    exit()

soup = bs4(re.text, 'html.parser')
 
make_file('Links.txt')

repetidos = []
for x in soup.find_all('a'):
    link = x['href']
    if domain in link:
        if link in repetidos:
            pass
        else:
            filter_url(link)
            save_a_link(link)
            if link not in repetidos:
                repetidos.append(link)
    else:
        direto = link.split('/')[0]
        formado = protocoloHTTP+'://'+domain+'/'+direto
        if formado in repetidos:
            pass
        else:
            filter_url(formado)
            save_a_link(formado)
            if formado not in repetidos:
                repetidos.append(formado)

input('\n\nUrl\'s save with sucess! > Links.txt')