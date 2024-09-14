# urls.py
from django.urls import path
from .views import GetWebSocketConnectionView

urlpatterns = [
    # Get WebSocket connection details
    path('api/chat/websocket/<str:app_type>/', GetWebSocketConnectionView.as_view(), name='get_websocket_connection'),
]
