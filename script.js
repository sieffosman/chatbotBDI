const chatOutput = document.getElementById('chat-output');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', () => {
    const userQuery = userInput.value;
    if (userQuery !== '') {
        chatOutput.innerHTML += `<p>User: ${userQuery}</p>`;
        userInput.value = '';

        // Send user query to the server
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_input: userQuery })
        })
        .then(response => response.json())
        .then(data => {
            chatOutput.innerHTML += `<p>Chatbot: ${data.response}</p>`;
        });
    }
});
