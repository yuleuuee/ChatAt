from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json
# ********************************* : WebsocketConsumer :**************************************************** #

class MyWebsocketConsumer(WebsocketConsumer):

    
    # This function get called when client opens the connection and is about to do handshake
    def connect(self):
        print('------------------------------------------------ WebsocketConsumer ::: connect function')
        print('Websocket Connected ...')

        self.group_name = self.scope['url_route']['kwargs']['groupko_name']

        # Join room group
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
        self.send(text_data='Message from server to client') # when server wants to send data to client

        text_data_json = json.loads(text_data)
        message = text_data_json['msg']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

       




# ********************************* : AsyncWebsocketConsumer :**************************************************** #
        
class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print('------------------------------------------------ WebsocketConsumer ::: connect function')
        print('Websocket Connected ...')
        await self.accept() # this keeps hendshanke(connected)
        # self.close()      
        
    async def receive(self, text_data=None, bytes_data=None):
        print('------------------------------------------------ WebsocketConsumer ::: receive function')
        print('Message received from client ...',text_data)
        await self.send(text_data='Message from server to client') # when server wants to send data to client
        # await self.close(code = 4321)      

    async def disconnect(self, close_code):
        print('------------------------------------------------ WebsocketConsumer ::: disconnect function')
        print('Websocket Disconnected ...',close_code)
        
