from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .models import CustomUser
from .forms import CustomUserChangeForm


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("profile_edit")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # Автоматический вход в систему после успешной регистрации
        return response


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'app/profile_edit.html'  # Замените на имя вашего шаблона
    success_url = reverse_lazy('profile_edit')  # Замените на имя вашего URL-пути редактора профиля

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        # Добавьте обработку изображения перед сохранением формы
        form.instance.profile_picture = self.request.FILES.get('profile_picture')
        return super().form_valid(form)


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


@login_required(login_url='login/')
def profile_edit(request):
    return render(request, 'app/profile_edit.html')
