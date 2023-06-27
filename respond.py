import sys
import json
from gensim.models import Word2Vec

# Carregar o modelo Word2Vec
model = Word2Vec.load("word2vec.model")

# Obter a mensagem do usuário como argumento
user_message = sys.argv[1]

# Dividir a mensagem do usuário em palavras
user_words = user_message.split()

try:
    # Tentar codificar a mensagem do usuário como um vetor
    user_vector = sum(model.wv[word] for word in user_words) / len(user_words)
except KeyError as e:
    # Se uma palavra não for encontrada, buscar a palavra mais semelhante
    missing_word = str(e).split("'")[1]  # Extrair a palavra que causou o erro
    most_similar_word = model.wv.most_similar(positive=[missing_word], topn=1)[0][0]
    print(f"A palavra '{missing_word}' não foi encontrada, a palavra mais similar é '{most_similar_word}'.")

# Encontrar a palavra mais semelhante ao vetor da mensagem do usuário
most_similar_word = model.wv.most_similar([user_vector], topn=1)[0][0]

# Imprimir a palavra mais semelhante
print(most_similar_word)
