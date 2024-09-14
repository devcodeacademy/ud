class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the app type and user_id from the WebSocket URL
        self.app_type = self.scope['url_route']['kwargs']['app_type']
        self.user_id = self.scope['url_route']['kwargs']['user_id']

        # Create a unique group for this chat room (app + user)
        self.group_name = f"{self.app_type}_chat_with_user_{self.user_id}"

        # Add this WebSocket connection to the group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        message_data = json.loads(text_data)
        message = message_data['message']

        # Send the message to the group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({'message': message}))

    async def disconnect(self, close_code):
        # Leave the group when disconnected
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
