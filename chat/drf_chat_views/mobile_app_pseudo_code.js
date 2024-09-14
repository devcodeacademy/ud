// Example using JavaScript (this will be translated to your mobile app's preferred framework)

// Step 1: Fetch WebSocket connection details from the API
async function getWebSocketDetails(appType) {
    const response = await fetch(`/api/chat/websocket/${appType}/`);
    const data = await response.json();

    const user_id = data.user_id;
    const websocket_url = data.websocket_url;

    // Step 2: Establish WebSocket connection
    const socket = new WebSocket(websocket_url);

    // Step 3: Handle incoming messages
    socket.onmessage = function(e) {
        const messageData = JSON.parse(e.data);
        // Display message in the chat
        console.log("Message received: ", messageData.message);
    };

    // Step 4: Send a message to the admin
    document.querySelector('#send-message-button').onclick = function() {
        const message = document.querySelector('#message-input').value;
        socket.send(JSON.stringify({'message': message}));
    };
}
