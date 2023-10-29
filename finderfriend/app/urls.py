from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='feed'),
    path('profile', views.profile, name='profile'),
    path('likes', views.likes, name='likes'),
    path('matches', views.matches, name='matches')
]