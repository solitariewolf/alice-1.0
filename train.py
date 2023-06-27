import sys
import json
from nltk.tokenize import word_tokenize

# Função para carregar as mensagens do arquivo JSON
def load_messages():
    try:
        with open('messages.json') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []  # retorna uma lista vazia se o arquivo estiver vazio

# Função para salvar as mensagens no arquivo JSON
def save_messages(messages):
    with open('messages.json', 'w') as file:
        json.dump(messages, file, indent=4)

# Função para adicionar uma nova mensagem
def add_message(messages, user_message):
    messages.append(user_message)
    save_messages(messages)

# Carregar as mensagens existentes
messages = load_messages()

# Obter a mensagem enviada pelo server.js como argumento
user_message = sys.argv[1]

# Tokenizar a mensagem do usuário
user_message = word_tokenize(user_message)

# Adicionar a mensagem do usuário às mensagens existentes
add_message(messages, user_message)

# Exibir as mensagens atualizadas
print('Mensagens atualizadas:')
for message in messages:
    print(message)
