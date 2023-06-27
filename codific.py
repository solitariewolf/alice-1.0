import json
from gensim.models import Word2Vec

# Carregar as mensagens
with open('messages.json', 'r') as file:
    messages = json.load(file)


# Treinar o modelo Word2Vec
model = Word2Vec(sentences=messages, vector_size=100, window=5, min_count=1, workers=4)

# Salvar o modelo
model.save("word2vec.model")
