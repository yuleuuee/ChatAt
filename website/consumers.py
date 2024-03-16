from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from . models import User,ChatMessage,Group
import json
from channels.db import database_sync_to_async

from . models import ChatMessage
# ********************************* : WebsocketConsumer :(wsc) **************************************************** #

class MyWebsocketConsumer(WebsocketConsumer):

    
    # This function get called when client opens the connection and is about to do handshake
    def connect(self):
        print('------------------------------------------------ WebsocketConsumer ::: connect function')
        print('Websocket Connected ...')

        self.group_name = self.scope['url_route']['kwargs']['groupko_name']
        print('Grpup name :::',self.group_name)
        # making a group and adding channels(users) to the group 
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept() # this keeps hendshanke(connected)
        

    # This function get called when the connetion is cut off 
    def disconnect(self, close_code):
        print('------------------------------------------------ WebsocketConsumer ::: disconnect function')
        print('Websocket Disconnected ...',close_code)
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        ) 

    # This function get called when data is received form client
    def receive(self, text_data=None, bytes_data=None):
        print('------------------------------------------------ WebsocketConsumer ::: receive function')
        print('Message received from client ...',text_data)
        # print('User ::: ',self.scope['user'])

        # text_data_json = json.loads(text_data) # converting string to python dict. is before using it ,  what we received is string : {'msg': 'hello'}
        # message = text_data_json['msg']


        data = json.loads(text_data)
        # Extract the message and sender's username
        message = data.get('msg')
        sender_username = self.scope['user'].username



        

        # -------------------------------------- #
        # Split the group name by underscores(groupname eg: ChatGroup_of_userX_userY)
        parts = self.group_name.split("_")

        # Extract the numbers after "userX" and "userY"
        numX = int(parts[2].replace("user", ""))
        numY = int(parts[3].replace("user", ""))

        if numX == self.scope['user'].id:
            receiver_id = numY
        else:
            receiver_id = numX

        print("Sender id:",self.scope['user'].id)
        print("Receiver id:",receiver_id)

        # Get the receiver's user object
        receiver = User.objects.get(id=receiver_id)
        sender =self.scope['user']
        print(sender)
        print(receiver)



        data=json.loads(text_data)
        print('Type of data',type(data))

        data['user']=self.scope['user'].username
        print(data)

        # -------------------------------------- #

        group = Group.objects.get(group_name= self.group_name) # getting the group which is the same as the group name 

        # saving the message to the database
        # new_chat = ChatMessage(sender=sender,receiver=receiver,message=message,group=group)
        # new_chat.save()

        # Send message to the group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'chat.message',
                'message': message,
                'sender_username': sender_username,
            }
        )

    # Receive message from group and send to the client side WebSocket (server sending message to client,js )
    def chat_message(self, event):
        message = event['message'],
        sender_username = event['sender_username']
        print('Type of data....:::::',type(message))
        # print(data)

        self.send(text_data=json.dumps({'message': message,'sender_username': sender_username})) # converting the dict. to string before sending to client


# ********************************* : AsyncWebsocketConsumer :(awsc) **************************************************** #
class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print('------------------------------------------------ AsyncWebsocketConsumer ::: connect function')
        print('Websocket Connected ...')
        self.group_name = self.scope['url_route']['kwargs']['groupko_name']

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        print('------------------------------------------------ AsyncWebsocketConsumer ::: receive function')
        print('Message received from client ...',text_data)
        
        text_data_json = json.loads(text_data)
        message = text_data_json['msg']

        # -------------------------------------- #
        # Split the group name by underscores (groupname eg: ChatGroup_of_userX_userY)
        parts = self.group_name.split("_")

        # Extract the numbers after "userX" and "userY"
        numX = int(parts[2].replace("user", ""))
        numY = int(parts[3].replace("user", ""))

        sender_id = self.scope['user'].id
        receiver_id = numY if numX == sender_id else numX

        print("Sender id:", sender_id)
        print("Receiver id:", receiver_id)

        # Get the sender and receiver's user objects
        sender = self.scope['user']
        receiver = await database_sync_to_async(User.objects.get)(id=receiver_id)

        # -------------------------------------- #

        group = await database_sync_to_async(Group.objects.get)(group_name=self.group_name)

        # Save the message to the database
        new_chat = ChatMessage(sender=sender, receiver=receiver, message=message, group=group)
        await database_sync_to_async(new_chat.save)()

        # Send message to the group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    async def disconnect(self, close_code):
        print('------------------------------------------------ AsyncWebsocketConsumer ::: disconnect function')
        print('Websocket Disconnected ...', close_code)
        
        # Leave chat group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def chat_message(self, event):
        message = event['message']

        # Send message data to the client
        await self.send(text_data=json.dumps({
            'message': message,
        }))
