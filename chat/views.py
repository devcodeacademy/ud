# views.py
from django.shortcuts import render
from django.views import View

class AdminChatView(View):
    def get(self, request, app_type, user_id):
        # Render the chat interface for admins
        return render(request, 'chat/admin_chat.html', {
            'app_type': app_type,
            'user_id': user_id,
        })

class UserChatView(View):
    def get(self, request, app_type):
        # Render the chat interface for users
        # Generate a unique user_id if the user is unregistered
        user_id = request.user.id if request.user.is_authenticated else 'guest_' + str(uuid.uuid4())
        return render(request, 'chat/user_chat.html', {
            'app_type': app_type,
            'user_id': user_id,
        })
