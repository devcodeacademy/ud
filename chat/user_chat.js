// user_chat.js
const app_type = '{{ app_type }}';
const user_id = '{{ user_id }}';  // dynamically assigned for unregistered users
const socket = new WebSocket(`ws://yourdomain.com/ws/admin/${app_type}/chat/${user_id}/`);

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').value += data.message + '\n';
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    socket.send(JSON.stringify({'message': message}));
    messageInputDom.value = '';
};
