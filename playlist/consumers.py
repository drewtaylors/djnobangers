from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PlaylistConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'playlist_%s' % self.room_name

        # join playlist room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # send message to group room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'playlist_message',
                'message': message
            }
        )

    # Receive message from room group
    async def playlist_message(self, event):
        message = event['message']

        # Send message to Websocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
