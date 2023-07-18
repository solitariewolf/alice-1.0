Projeto Chatbot (Beta) 🤖

Este projeto implementa um chatbot usando uma abordagem baseada em redes neurais LSTM (Long Short-Term Memory) 🧠. O chatbot é capaz de gerar respostas com base nas mensagens fornecidas pelos usuários 💬.

Componentes do Projeto 📦

respond.py 📝: O script respond.py é responsável por gerar uma resposta a partir de um texto inicial fornecido pelo usuário (também chamado de "texto semente"). Ele carrega um modelo LSTM treinado e um tokenizer do disco e, em seguida, usa o modelo para gerar uma sequência de 10 palavras a partir do texto semente. A sequência é gerada adicionando uma palavra de cada vez, onde cada palavra é a palavra com a maior probabilidade de acordo com o modelo. O script retorna a sequência gerada como a resposta do chatbot.

train.py 🏋️‍♂️: O script train.py é responsável por adicionar novas mensagens dos usuários ao conjunto de treinamento do chatbot. Ele recebe uma mensagem do usuário como entrada, tokeniza a mensagem e, em seguida, adiciona a mensagem tokenizada ao arquivo 'messages.json'. Este arquivo armazena todas as mensagens dos usuários que são usadas para treinar o chatbot.

codific.py 🤖: O script codific.py é onde o modelo LSTM do chatbot é construído e treinado. Ele carrega as mensagens dos usuários do arquivo 'messages.json', tokeniza as mensagens e, em seguida, transforma as mensagens em sequências de números que podem ser alimentadas para o modelo. O script, em seguida, constrói um modelo LSTM, compila o modelo e o treina nas sequências. Após o treinamento, o script salva o modelo e o tokenizer no disco para uso posterior.

server.js 🌐: O script server.js é o servidor principal que lida com as solicitações HTTP. Ele usa o framework Express.js para criar um servidor web e o módulo 'child_process' para chamar os scripts Python train.py e respond.py como subprocessos. O servidor tem um único endpoint '/message', que aceita mensagens dos usuários e, em seguida, chama train.py ou respond.py com base no modo de treinamento fornecido na solicitação. Se o modo de treinamento for verdadeiro, train.py é chamado com a mensagem do usuário. Se o modo de treinamento for falso, respond.py é chamado com a mensagem do usuário, e a resposta gerada pelo respond.py é retornada como resposta à solicitação HTTP.

Como usar 🚀
Certifique-se de ter o Python 3 e as bibliotecas necessárias instaladas (consulte requirements.txt). Execute o script codific.py para treinar o modelo inicial do chatbot:
```
python3 codific.py
```
Inicie o servidor:
```
node server.js
```
Acesse o chatbot através do navegador usando o endereço http://localhost:5000. Digite uma mensagem no chat e aguarde a resposta do chatbot.

Atualize o arquivo respond.py para usar o modo de resposta personalizado ao gerar a resposta.

Contribuição ✨
Sinta-se à vontade para contribuir com este projeto abrindo problemas ou enviando pull requests. Sua contribuição é bem-vinda! 🙌

Licença 📜
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

Importante ❗
Este chatbot está em fase de treinamento e contém algumas palavras já incluídas em seu treinamento. No entanto, é importante ressaltar que não nos responsabilizamos pelo uso indevido do chatbot. Recomendamos que ele seja utilizado apenas para fins educacionais 🎓. Além disso, todo o conteúdo utilizado para treinar o chatbot deve ser devidamente licenciado e respeitar os direitos autorais.⚠️
