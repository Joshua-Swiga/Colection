import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chatapp.models import *
from .models import *


class ChatConsumer(AsyncWebsocketConsumer):
    # We now need to create a connect method
    # This is an asyncronous function
    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json

        print(message)


    async def send_message(self, event):
        data = event['message']

        await self.create_message(data=data)
        response_data = {
            'sender' : data['sender'],
            'message' : data['message'],
        }

        await self.send(text_data=json.dumps({'message': response_data}))


    # This will save the data to the database. 
    @database_sync_to_async
    def create_message(self, data):
        get_room_by_name = Room.objects.get(room_name=data['room_name'])
        if not Messages.objects.filter(message=data['message']).exists():
            new_message = Messages(room=get_room_by_name, sender=data['sender'], message=data['message'])
            new_message.save()