from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<notification>\w+)/$", consumers.AsyncNotificationConsumer.as_asgi())
]