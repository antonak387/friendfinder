from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from .models import Likes
from .forms import CustomUserCreationForm
from django.contrib.auth import login


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("feed")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # Автоматический вход в систему после успешной регистрации
        return response


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
