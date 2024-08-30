// static/js/chat.js
console.log("here")
function addMessage(sender, message) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatMessages.appendChild(messageDiv);
    // Scroll to bottom of chat container
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Function to handle sending a message
function sendMessage() {
    const userInput = document.getElementById('user-message');
    console.log(userInput)
    const message = userInput.value.trim();
    if (message !== '') {
        addMessage('You', message);
        // Reset user input
        userInput.value = '';
        // Send message to API
        fetch('/chat/', {  // Update the URL to match Django's URL pattern
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message
            })
        })
        .then(response => response.json())
        .then(data => {
            const apiResponse = data.response;
            addMessage('FarmAsisst', apiResponse);
        })
        .catch(error => console.error('Error:', error));
    }
}

// Event listener for pressing enter in the input field
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('user-message').addEventListener('keydown', function (event) {
        console.log('Key pressed:', event.key);
        if (event.key === 'Enter') {
            console.log("Enter pressed");
            sendMessage();
        }
    });
});