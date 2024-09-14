# serializers.py
from rest_framework import serializers

class WebSocketConnectionSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    websocket_url = serializers.CharField()
