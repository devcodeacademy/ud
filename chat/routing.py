# routing.py
from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/admin/(?P<app_type>\w+)/chat/(?P<user_id>\w+)/$', ChatConsumer.as_asgi()),
]
