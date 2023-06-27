const { spawn } = require('child_process');
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

app.use(express.static(__dirname));


// Função para enviar mensagem para o train.py
function sendMessageToTrain(message) {
    const trainProcess = spawn('python3', ['train.py', message]);
  
    trainProcess.stdout.on('data', (data) => {
      console.log(`Resultado do treinamento: ${data}`);
    });
  
    trainProcess.stderr.on('data', (data) => {
      console.error(`Erro no treinamento: ${data}`);
    });
  }

  // Função para enviar mensagem para o respond.py
  function sendMessageToRespond(message, callback) {
    const respondProcess = spawn('python3', ['respond.py', message]);
  
    respondProcess.stdout.on('data', (data) => {
      // Aqui você precisa lidar com a resposta do respond.py e passá-la para o callback
      callback(data.toString());
    });
  
    respondProcess.stderr.on('data', (data) => {
      console.error(`Erro na resposta: ${data}`);
      
      // Aqui você pode adicionar lógica para lidar com erros específicos
      if (data.toString().includes("Key '")) {
        const word = data.toString().split("'")[1];  // Extrair a palavra que causou o erro
        console.error(`A palavra '${word}' não foi encontrada no vocabulário do modelo.`);
      }
    });
  }
  
  app.post('/message', (req, res) => {
    const userMessage = req.body.message;
    const trainMode = req.body.trainMode;  // Obter o estado da caixa de seleção

    // Verificar se o modo de treinamento está ativado
    if (trainMode) {
      // Enviar a mensagem para o train.py
      sendMessageToTrain(userMessage);
    } else {
      // Enviar a mensagem para o respond.py e obter a resposta do bot
      sendMessageToRespond(userMessage, (botResponse) => {
        // Enviar a resposta do bot ao usuário
        res.json({ response: botResponse });
      });
    }
});


app.listen(5000, () => {
    console.log('Servidor iniciado na porta 5000');
});
