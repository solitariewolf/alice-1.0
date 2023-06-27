document.addEventListener('DOMContentLoaded', function() {
  var userInput = document.getElementById('user-input');
  var sendButton = document.getElementById('send-button');
  var messageArea = document.getElementById('message-area');

  sendButton.addEventListener('click', sendMessage); // Chamando a função sendMessage ao clicar no botão

  userInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
      event.preventDefault(); // Evitando quebra de linha na caixa de texto
      sendMessage(); // Chamando a função sendMessage ao pressionar a tecla "Enter"
    }
  });

  function sendMessage() {
    var userMessage = userInput.value;
    userInput.value = '';
    
    // Obter o estado da caixa de seleção
    var trainMode = document.getElementById('train-mode').checked;

    var userDiv = document.createElement('div');
    userDiv.textContent = 'Você: ' + userMessage;
    messageArea.appendChild(userDiv);

    fetch(window.location.origin + '/message', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        message: userMessage,
        trainMode: trainMode  // Enviar o estado da caixa de seleção
      })
    }).then(response => response.json())
      .then(data => {
        var botDiv = document.createElement('div');
        botDiv.textContent = 'Alice: ' + data['response'];
        messageArea.appendChild(botDiv);
      });
  }

});