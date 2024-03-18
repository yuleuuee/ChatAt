# This file get connected to javascript in frontend and consumer.py in the backend
# And this 'routing.py' is the container file of 'asgi.py' file of the project directory
from django.urls import path 
from . import consumers

websocket_urlpatterns =[
    path('ws/wsc/<str:groupko_name>/',consumers.MyWebsocketConsumer.as_asgi()),
    path('ws/awsc/<str:groupko_name>/',consumers.MyAsyncWebsocketConsumer.as_asgi()),

    path('ws/wsc/',consumers.Public_WebsocketConsumer.as_asgi()),
]