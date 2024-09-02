# urls.py
from django.urls import path
from .views import PremisesList, PremisesDetail

urlpatterns = [
    path('premises/', PremisesList.as_view(), name='premises-list'),
    path('premises/<int:pk>/', PremisesDetail.as_view(), name='premises-detail'),
]
