# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import uuid4

class GetWebSocketConnectionView(APIView):
    def get(self, request, app_type):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            # If the user is not authenticated, generate a unique guest user ID
            user_id = f"guest_{uuid4()}"

        # WebSocket URL format for the chat connection
        websocket_url = f"ws://yourdomain.com/ws/admin/{app_type}/chat/{user_id}/"

        # Return user_id and websocket_url to the client
        return Response({
            "user_id": user_id,
            "websocket_url": websocket_url
        }, status=status.HTTP_200_OK)



# 3. Testing API
# Test the API with an HTTP request to verify that it returns
# the correct WebSocket connection details.
#
# GET /api/chat/websocket/rental/
#
#
# Expected Response:
# {
#     "user_id": "guest_f4f44b0c-5b0f-4858-b245-478a4e5f4183",
#     "websocket_url": "ws://yourdomain.com/ws/admin/rental/chat/guest_f4f44b0c-5b0f-4858-b245-478a4e5f4183/"
# }