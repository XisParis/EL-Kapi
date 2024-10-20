# Código Base do GROQ

Este módulo implementa a biblioteca fundamental para um uso de Inteligência Artificial (IA) utilizando o cliente Groq. A Biblioteca facilita interações com funcionalidades de IA, permitindo que desenvolvedores integrem modelos de aprendizado de máquina e recursos orientados por IA em suas aplicações.

## Uso

Para utilizar esta biblioteca, primeiro importe ela:

```python
from groq import Groq
```

Agora, obtenha sua chave API em: https://console.groq.com/keys

Com a chave API em mãos, defina o client GROQ com sua API:

```python
client = Groq(api_key='your_groq_api_key')
```

Agora, defina o modelo e outros fatores da IA:

```python
completion = client.chat.completions.create(
    model="llama-3.1-70b-versatile", # Model
    messages=[
        {
            "role": "system",
            "content": "Preciso de uma resposta direta e profissional!"
        },
        {
            "role": "user",
            "content": "Olá qual seu modelo de IA?"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)
```

A resposta ja foi gerada, com base no que o usuario perguntou, então iremos printar ela.

```python
resposta = ''
for chunk in completion:
    resposta += chunk.choices[0].delta.content or ""
```

Já temos a resposta armazenada na variavel "resposta", agora faça o que quiser com ela.