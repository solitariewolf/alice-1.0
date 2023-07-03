from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
from keras.optimizers import RMSprop
from keras.utils import to_categorical
import numpy as np
import json
import io

# Carregar as mensagens
with open('pdf.json', 'r') as file:
    messages = json.load(file)

# Preparar o Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(messages)

# Transformar o texto em sequências de números
sequences = tokenizer.texts_to_sequences(messages)

# Obter o número total de palavras
num_words = len(tokenizer.word_index) + 1

# Preparar os dados de entrada e saída
X = []
y = []
for sequence in sequences:
    for i in range(1, len(sequence)):
        X.append(sequence[:i])
        y.append(sequence[i])
X = np.array(X)
y = np.array(y)

# Preencher as sequências para terem o mesmo comprimento
max_length = max(len(x) for x in X)
X = pad_sequences(X, maxlen=max_length)

# Depois que as sequências são preenchidas, elas podem ser convertidas em um array numpy regular
X = np.array(X)

# One-hot encoding das saídas
y = to_categorical(y, num_classes=num_words)

# Construir o modelo LSTM
model = Sequential()
model.add(Embedding(num_words, 100, input_length=max_length))
model.add(LSTM(100))
model.add(Dense(num_words, activation='softmax'))

# Compilar o modelo
model.compile(loss='categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])

# Treinar o modelo
model.fit(X, y, epochs=10, verbose=2)

# Salvar o modelo
model.save("lstm_model.h5")

# Salvar o tokenizer como um arquivo JSON
tokenizer_json = tokenizer.to_json()
with io.open('tokenizer.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(tokenizer_json, ensure_ascii=False))
