"""
ASGI config for demo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

import django

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

from Chat import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()
application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": application,
    "websocket": URLRouter(routing.websocket_urlpatterns)
})


