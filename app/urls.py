from django.urls import path, include
from app.views import RegisterClient

urlpatterns = [
    path('api/clients/create', RegisterClient.as_view(), name='register')
]