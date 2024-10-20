from groq import Groq

client = Groq(api_key='your_api_key')

completion = client.chat.completions.create(
    model="llama-3.1-70b-versatile", # Modelo de IA groq
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

resposta = ''
for chunk in completion:
    resposta += chunk.choices[0].delta.content or ""

print(resposta)
