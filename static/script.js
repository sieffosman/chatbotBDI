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
