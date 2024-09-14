# urls.py
from django.urls import path
from .views import AdminChatView, UserChatView

urlpatterns = [
    # Admin chat URLs
    path('admin/rental/chat/<str:user_id>/', AdminChatView.as_view(app_type='rental'), name='rental_admin_chat'),
    path('admin/kindergarten/chat/<str:user_id>/', AdminChatView.as_view(app_type='kindergarten'),
         name='kindergarten_admin_chat'),

    # User chat URLs (for users to message admins)
    path('rental/chat/', UserChatView.as_view(app_type='rental'), name='rental_user_chat'),
    path('kindergarten/chat/', UserChatView.as_view(app_type='kindergarten'), name='kindergarten_user_chat'),
]
