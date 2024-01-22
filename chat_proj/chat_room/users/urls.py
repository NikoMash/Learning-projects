from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('users/user_details/<int:id>', views.user_details, name='user_details'),
    path('chat/', views.chat, name='chat'),
    path('testing/', views.testing, name='testing'),  
]