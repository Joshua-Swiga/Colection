
import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from chatapp import routing

from django.core.asgi import get_asgi_application



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_chat.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(
        routing.websocket_urlpatterns # This is being registered from routing.py file
    )
})
