from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='feed'),
    path('profile', views.profile_view, name='profile'),
    path('likes', views.likes, name='likes'),
    path('matches', views.matches, name='matches'),
    path('profile_edit', views.ProfileEditView.as_view(), name='profile_edit'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('like_user/<int:user_id>/', views.like_user, name='like_user'),
    path('chat/<int:match_id>/', views.chat, name='chat'),
    path('send', views.send, name='send'),
    path('getMessages/<int:match_id>/', views.getMessages, name='getMessages'),
    path('ads', views.ads, name='ads'),
    path('send_ads', views.send_ads, name='send_ads'),
    path('getAds', views.getAds, name='getAds'),
]