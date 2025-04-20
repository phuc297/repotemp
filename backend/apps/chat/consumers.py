import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import get_object_or_404
from .models import Message, Conversation
from apps.users.models import Profile
from asgiref.sync import sync_to_async


class AsyncChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.conversation_id = self.scope["url_route"]["kwargs"]["conversation_id"]
        self.room_group_name = f"chat_{self.conversation_id}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        conversation_id = text_data_json["conversation_id"]
        sender_id = text_data_json["sender_id"]
        receiver_id = text_data_json["receiver_id"]
        content = text_data_json["content"]

        conversation = await get_conversation(conversation_id)
        sender = await get_profile(sender_id)
        receiver = await get_profile(receiver_id)
        message = await sync_to_async(Message.objects.create)(
            conversation=conversation, sender=sender, receiver=receiver, content=content)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat.message",
                'sender_id': message.sender.id,
                'content': message.content,
                'avatar': message.sender.avatar.url
            })

    # Receive message from room group
    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "content": event["content"],
            "sender_id": event["sender_id"],
            "avatar": event["avatar"]
        }))


@sync_to_async
def get_conversation(conversation_id):
    return Conversation.objects.get(pk=int(conversation_id))


@sync_to_async
def get_profile(profile_id):
    return Profile.objects.get(pk=int(profile_id))
