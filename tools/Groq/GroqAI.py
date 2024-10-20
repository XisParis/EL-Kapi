from groq import Groq
import os

models = 'llama-3.1-70b-versatile' # Model

class F:
    GREEN = '\033[32m'
    RED = '\033[31m'
    RESET = '\033[0m'
    CYAN = '\033[1;36m'
    ORANGE = '\033[38;5;214m'

def banner():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(F.CYAN+f"""
   __________  ____  ____        ___    ____
  / ____/ __ \/ __ \/ __ \      /   |  /  _/
 / / __/ /_/ / / / / / / /     / /| |  / /  
{F.RESET+F.RED}/ /_/ / _, _/ /_/ / /_/ /     / ___ |_/ /   
\____/_/ |_|\____/\___\_\    /_/  |_/___/ {F.CYAN}{models}
"""+F.RESET)

historico = ['']

def get_response(text, history=False):
    client = Groq(api_key='your_api_key')

    if len(historico) > 20: # Aumente se quiser um historico mais prolongado, obs: quanto maior o historico, pode fazer a IA nao responder muito bem.
        historico.clear()

    if history == True:
        content = 'Leve isso como historico de nossas conversas, não fale nada sobre o historico, apenas se eu perguntar:'+str(historico)+'\n'+text
    else:
        content = text

    completion = client.chat.completions.create(
        model=models,
        messages=[
            {
                "role": "system",
                "content": "responda de forma direta e rapida."
            },
            {
                "role": "user",
                "content": content
            }
        ],
        temperature=1, 
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    
    resp = ''
    for chunk in completion:
        resp += chunk.choices[0].delta.content or ""

    historico.append('Eu falei: '+text+' Voce respondeu: '+resp)
    return resp

def main():
    banner()

    answer = str(input(f'[{F.ORANGE}GROQ{F.RESET}]: Qual sua pergunta?\n> ')).strip()

    print(f'\n[{F.GREEN}YOU{F.RESET}]: '+answer+'\n')

    print('Generating response...', end='\r')

    response = get_response(text=answer, history=True)

    print(' ' * 90, end='\r')
    
    print(f'[{F.ORANGE}GROQ{F.RESET}]: '+response)

    input(f'\n[{F.CYAN}SYSTEM{F.RESET}]: Enter para fazer mais uma pergunta.')
    main()

if __name__ == '__main__':
    main()
