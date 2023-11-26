from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from .models import Likes


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required(login_url='login/')
def index(request):
    return render(request, 'app/index.html')


@login_required(login_url='login/')
def profile_view(request):
    return render(request, 'app/profile.html')


@login_required(login_url='login/')
def likes(request):
    return render(request, 'app/likes.html')


@login_required(login_url='login/')
def matches(request):
    return render(request, 'app/likes.html')


