def chat(text):
    response = requests.post('https://api.openai.com/v1/engines/davinci/jobs',
        headers={'Content-Type': 'application/json'},
        data=json.dumps({'text': text, 'max_tokens': 100}),
        auth=('YOUR_API_KEY', '')
    )
    return response.json()['choices'][0]['text']

print('Bienvenido al ChatGPT, ¿en qué puedo ayudarte hoy?')

while True:
    text = input('> ')
    if text.strip().lower() == 'bye':
        print('Adiós!')
        break
    else:
        print(chat(text))
