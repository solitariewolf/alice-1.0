from keras.preprocessing.text import tokenizer_from_json
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
from keras_preprocessing.sequence import pad_sequences
import numpy as np
import sys
import json
import io

# Função para gerar uma frase
def generate_sentence(model, tokenizer, seed_text, max_length):
    # Inicializar a frase gerada com o texto semente
    generated = seed_text

    # Gerar 10 palavras
    for _ in range(10):
        # Codificar o texto como uma sequência de números
        encoded = tokenizer.texts_to_sequences([generated])[0]
        # Preencher a sequência para que tenha o mesmo comprimento que as sequências de treinamento
        encoded = pad_sequences([encoded], maxlen=max_length, padding='pre')

        # Prever a próxima palavra
        probabilities = model.predict(encoded, verbose=0)[0]
        predicted_word_index = np.argmax(probabilities)

        # Procurar a palavra prevista no dicionário do tokenizer
        for word, index in tokenizer.word_index.items():
            if index == predicted_word_index:
                generated += ' ' + word
                break

    return generated

# Carregar o modelo e o tokenizer
model = load_model('lstm_model.h5')
with open('tokenizer.json', 'r') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)

# Obter a mensagem do usuário como argumento
seed_text = sys.argv[1]

# Definir o comprimento máximo da frase
max_length = 411

# Gerar uma frase
sentence = generate_sentence(model, tokenizer, seed_text, max_length)

# Imprimir a frase
print(sentence)
