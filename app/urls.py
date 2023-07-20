from django.urls import path
from app.views import RegisterClient, client_view, LoginUser, logout_user, like
from django.views.generic import TemplateView

urlpatterns = [
    path('api/clients/create', RegisterClient.as_view(), name='register'),
    path('api/clients/', client_view, name='client_view'),
    path('api/clients/login', LoginUser.as_view(), name='login'),
    path('', TemplateView.as_view(template_name='main_menu.html'), name='main_menu'),
    path('api/clients/logout', logout_user, name='logout'),
    path('api/clients/<int:pk>/match', like, name='like')
]
