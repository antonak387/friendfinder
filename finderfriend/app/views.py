from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Likes

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

@login_required
def profile_view(request):
    return render(request, 'app/profile.html')


def likes(request):
    return render(request, 'app/likes.html')


def matches(request):
    return render(request, 'app/likes.html')
