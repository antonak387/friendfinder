from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='feed'),
    path('profile', views.profile_view, name='profile'),
    path('likes', views.likes, name='likes'),
    path('matches', views.matches, name='matches')
]