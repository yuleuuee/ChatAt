from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from . models import User,ChatMessage,Group
import json
from channels.db import database_sync_to_async
from . models import ChatMessage

from . models import Post,Like,Comment,UserProfile

from asgiref.sync import sync_to_async


# ********************************* :: WebsocketConsumer :(wsc), for Real time Chat :: **************************************************** #

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

        data = json.loads(text_data) # converting string to python dict. is before using it ,  what we received is string : {'msg': 'hello'}
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
        print('Grpup name :::', self.group_name)
        # making a group and adding channels(users) to the group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()  # this keeps handshake(connected)

    async def disconnect(self, close_code):
        print('------------------------------------------------ AsyncWebsocketConsumer ::: disconnect function')
        print('Websocket Disconnected ...', close_code)
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        print('------------------------------------------------ AsyncWebsocketConsumer ::: receive function')
        print('Message received from client ...', text_data)

        data = json.loads(text_data)
        message = data.get('msg')
        sender_username = self.scope['user'].username

        parts = self.group_name.split("_")
        numX = int(parts[2].replace("user", ""))
        numY = int(parts[3].replace("user", ""))
        if numX == self.scope['user'].id:
            receiver_id = numY
        else:
            receiver_id = numX

        print("Sender id:", self.scope['user'].id)
        print("Receiver id:", receiver_id)

        receiver = await sync_to_async(User.objects.get)(id=receiver_id)
        sender = self.scope['user']

        data['user'] = sender_username

        group = await sync_to_async(Group.objects.get)(group_name=self.group_name)

        # saving the message to the database
        # new_chat = ChatMessage(sender=sender,receiver=receiver,message=message,group=group)
        # new_chat.save()

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat.message',
                'message': message,
                'sender_username': sender_username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender_username = event['sender_username']
        print('Type of data....:::::', type(message))

        await self.send(text_data=json.dumps({'message': message, 'sender_username': sender_username}))


# ******************************************************************************************************************************************************************
# # ********************************* :: Public page : WebsocketConsumer :(wsc) , For like and Comment Part :: **************************************************** #
# ******************************************************************************************************************************************************************
    
class Public_WebsocketConsumer(WebsocketConsumer):

    def connect(self):
        print('------------------------------------------------ Public_page_WebsocketConsumer ::: connect function ::: Websocket Connected ...')
        self.group_name = 'public_page'
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        print('------------------------------------------------ Public_page_WebsocketConsumer ::: disconnect function ::: Websocket Disconnected ...')
        print('Websocket Disconnected ...', close_code)
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        print('------------------------------------------------ Public_page_WebsocketConsumer::: receive function')
        print('Message received from client ...', text_data)
        try:
            data = json.loads(text_data)
            user = self.scope['user']
            user_id = user.id

            # like part :
            if 'po_id' in data:
                # For handling 'po_id'
                post_id = data.get('po_id')
                post = Post.objects.get(id=post_id)
                like_filter = Like.objects.filter(post_id=post_id, user_id=user_id).first()

                if like_filter is None:
                    self.create_like(post, user)
                else:
                    self.delete_like(like_filter, post)
                
                no_of_likes = post.no_of_likes

                async_to_sync(self.channel_layer.group_send)(
                    self.group_name,
                    {
                        'type': 'public.data',
                        'no_of_likes': no_of_likes,
                        'like_post_id': post_id,
                        'user_liked_id': user_id,
                    }
                )

            # comment part :
            if 'post_id' in data:
                # For handling 'post_id'
                post_id = data.get('post_id')
                post_for_cmt = Post.objects.get(id=post_id)

                cmt_content = data.get('cmt_content')
                self.create_comment(post_for_cmt, user_id, cmt_content)

                no_of_comments = post_for_cmt.no_of_comments
                
                async_to_sync(self.channel_layer.group_send)(
                    self.group_name,
                    {
                        'type': 'public.data',
                        'no_of_comments': no_of_comments,
                        'cmt_post_id': post_id,
                        'user_comented_id': user_id,
                        'cmt_content': cmt_content,
                    }
                )
            
            # Dark mode part :
            if 'is_dark' in data:
                user_profile = UserProfile.objects.get(user=self.scope['user'])
                user_profile.dark_mode = data.get('is_dark')
                user_profile.save()
                async_to_sync(self.channel_layer.group_send)(
                    self.group_name,
                    {
                        'type': 'public.data',
                        'is_dark':data.get('is_dark'),
                    }
                )

        except json.JSONDecodeError:
            print("Invalid JSON data received.")
        except Post.DoesNotExist:
            print("Post does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def create_like(self, post, user):
        new_like = Like.objects.create(post=post, user=user)
        post.no_of_likes += 1
        post.save()
        new_like.save()

    def delete_like(self, like_filter, post):
        like_filter.delete()
        post.no_of_likes -= 1
        post.save()

    def create_comment(self, post_for_cmt, user_id, cmt_content):
        new_comment = Comment.objects.create(post=post_for_cmt, user_id=user_id, content=cmt_content)
        post_for_cmt.no_of_comments += 1
        post_for_cmt.save()
        new_comment.save()

    def public_data(self, event):
        try:
            no_of_likes = event.get('no_of_likes')
            like_post_id = event.get('like_post_id')
            user_liked_id = event.get('user_liked_id')

            no_of_comments = event.get('no_of_comments')
            cmt_post_id = event.get('cmt_post_id')
            user_comented_id = event.get('user_comented_id')
            cmt_content = event.get('cmt_content')

            is_dark = event.get('is_dark')

            self.send(text_data=json.dumps({
                'no_of_likes': no_of_likes,
                'like_post_id': like_post_id,
                 'user_liked_id': user_liked_id,

                'no_of_comments': no_of_comments,
                'cmt_post_id': cmt_post_id,
                'user_comented_id': user_comented_id,
                'cmt_content': cmt_content,
                
                'is_dark':is_dark,
            }))
        except Exception as e:
            print(f"An error occurred while sending data: {e}")
