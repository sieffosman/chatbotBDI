document.addEventListener('DOMContentLoaded', function () {
    const openChatButton = document.getElementById('open-chat');
    const closeChatButton = document.getElementById('close-chat');
    const chatWidget = document.getElementById('chat-widget');
    const sendButton = document.getElementById('send-button');
    const userInputField = document.getElementById('user-input');
    const chatOutput = document.getElementById('chat-output');

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

    sendButton.addEventListener('click', function () {
        handleUserInput();
    });

    // Add an event listener to handle user input when Enter key is pressed
    userInputField.addEventListener('keyup', function (event) {
        if (event.key === 'Enter') {
            handleUserInput();
        }
    });

    const sendUserInput = (userQuery) => {
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_input: userQuery })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.response); // Log the response received from the server

            // Simulate typing effect for chatbot response
            simulateTyping(data.response, chatOutput);
            userInputField.value = ''; // Clear the input field
        });
    }
    

    // Simulate typing effect
    function simulateTyping(response, outputElement) {
        const speed = 50; // Typing speed (adjust as needed)
        let index = 0;

        function type() {
            if (index < response.length) {
                outputElement.innerHTML += response.charAt(index);
                index++;
                setTimeout(type, speed);
            }
        }

        type();
    }

    // Handle user input submission
    function handleUserInput() {
        const userQuery = userInputField.value;
        chatOutput.innerHTML += `<p>Monty: ${userQuery}</p>`;
        simulateTyping("Chatbot response...", chatOutput); // Simulate typing effect for chatbot response

        // You can replace the placeholder text above with the actual chatbot response
        sendUserInput(userQuery); // Send user input to the server
    }
});
