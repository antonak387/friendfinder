from django.urls import path, include
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]