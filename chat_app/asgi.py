# """
# ASGI config for chat_app project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
# """

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')

# application = get_asgi_application()

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import website.routing

# this will solve the problem of the self.scope['user]
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yule01.settings')

application = ProtocolTypeRouter({
    'htttp':get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(website.routing.websocket_urlpatterns)),
})
