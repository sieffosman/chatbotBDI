document.addEventListener('DOMContentLoaded', function () {
    const openChatButton = document.getElementById('open-chat');
    const closeChatButton = document.getElementById('close-chat');
    const chatWidget = document.getElementById('chat-widget');

    openChatButton.addEventListener('click', function () {
        chatWidget.style.display = 'block';
        chatWidget.classList.remove('closed');
        chatWidget.classList.add('open');
    });

    closeChatButton.addEventListener('click', function () {
        chatWidget.style.display = 'none';
        chatWidget.classList.remove('open');
        chatWidget.classList.add('closed');
    });
});


const sendUserInput = () => {
    const userQuery = document.getElementById('user-input').value;

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_input: userQuery })
    })
    .then(response => response.json())
    .then(data => {
        const chatOutput = document.getElementById('chat-output');
        chatOutput.innerHTML += `<p>User: ${userQuery}</p>`;
        chatOutput.innerHTML += `<p>Monty: ${data.response}</p>`;
        document.getElementById('user-input').value = ''; // Clear the input field
    });
}

// Attach the function to the "Send" button's click event
document.getElementById('send-button').addEventListener('click', sendUserInput);
