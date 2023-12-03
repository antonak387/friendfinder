from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


@login_required('home')
def index(request):
    return render(request, 'app/index.html')


@login_required('home')
def profile_view(request):
    return render(request, 'app/profile.html')


@login_required('home')
def likes(request):
    return render(request, 'app/likes.html')


@login_required('home')
def matches(request):
    return render(request, 'app/likes.html')
