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
  function sendMessageToRespond(message, res) {
    let responseSent = false;
    const respondProcess = spawn('python3', ['respond.py', message]);
  
    respondProcess.stdout.on('data', (data) => {
      if (!responseSent) {
        responseSent = true;
        res.json({ response: data.toString() });
      }
    });
  
    respondProcess.stderr.on('data', (data) => {
      console.error(`Erro na resposta: ${data}`);
      
      if (data.toString().includes("Key '")) {
        const word = data.toString().split("'")[1];
        console.error(`A palavra '${word}' não foi encontrada no vocabulário do modelo.`);
      }
  
      if (!responseSent) {
        responseSent = true;
        res.status(500).json({ error: data.toString() });
      }
    });
  }
  
  
  app.post('/message', (req, res) => {
    const userMessage = req.body.message;
    const trainMode = req.body.trainMode;
  
    if (trainMode) {
      sendMessageToTrain(userMessage);
    } else {
      sendMessageToRespond(userMessage, res);
    }
});


app.listen(5000, () => {
    console.log('Servidor iniciado na porta 5000');
});
