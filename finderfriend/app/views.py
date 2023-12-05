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

from django.shortcuts import get_object_or_404
from .models import Likes
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


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
    success_url = reverse_lazy('profile')  # Замените на имя вашего URL-пути редактора профиля

    def get_object(self, queryset=None):
        return self.request.user


@login_required(login_url='login/')
def index(request):
    random_user = CustomUser.objects.order_by('?').first()

    context = {
        'user': random_user,
    }
    return render(request, 'app/index.html', context)


@login_required(login_url='login/')
def like_user(request, user_id):
    if request.method == 'POST':
        sender = request.user
        receiver = get_object_or_404(CustomUser, id=user_id)
        if not Likes.objects.filter(sender=sender, receiver=receiver).exists():
            Likes.objects.create(sender=sender, receiver=receiver)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@login_required(login_url='login/')
def profile_view(request):
    return render(request, 'app/profile.html')


@login_required(login_url='login/')
def likes(request):
    like_user_id = Likes.objects.order_by('?').filter(receiver_id=request.user).first()
    if like_user_id is not None:
        if like_user_id.sender_id != request.user.id:
            like_user_name = CustomUser.objects.get(id=like_user_id.sender_id)
            context = {
                'user': like_user_name,
            }
            return render(request, 'app/likes.html', context)
        else:
            context = {
                'user': 0
            }
            return render(request, 'app/likes.html', context)
    else:
        context = {
            'user': 0
        }
        return render(request, 'app/likes.html', context)



@login_required(login_url='login/')
def matches(request):
    return render(request, 'app/likes.html')


@login_required(login_url='login/')
def profile_edit(request):
    return render(request, 'app/profile_edit.html')
