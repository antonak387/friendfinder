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
    path('interests', views.interests, name='interests'),
    path('beer_club', views.beer_club, name='beer_club'),
    path('coffee_club', views.coffee_club, name='coffee_club'),
    path('walks_club', views.walks_club, name='walks_club'),
    path('games_club', views.games_club, name='games_club')
]