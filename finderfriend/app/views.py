from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.http import JsonResponse
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Likes, Matches


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
    while True:
        random_user = CustomUser.objects.order_by('?').first()
        if random_user != request.user:
            break

    context = {'user': random_user,}
    return render(request, 'app/index.html', context)


@login_required(login_url='login/')
def like_user(request, user_id):
    if request.method == 'POST':
        sender = request.user
        receiver = get_object_or_404(CustomUser, id=user_id)
        if not Likes.objects.filter(sender=sender, receiver=receiver).exists():
            Likes.objects.create(sender=sender, receiver=receiver)
            if Likes.objects.filter(sender=receiver, receiver=sender).exists() and not Matches.objects.filter(user2=sender, user1=receiver).exists() and not Matches.objects.filter(user2=receiver, user1=sender).exists():
                Matches.objects.create(user2=sender, user1=receiver, json_dialog={})
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
            context = {'user': like_user_name}
            return render(request, 'app/likes.html', context)
        else:
            context = {'user': -1}
            return render(request, 'app/likes.html', context)
    else:
        return render(request, 'app/no_likes.html')


@login_required(login_url='login/')
def matches(request):
    matches_user_name = []

    matches_user1 = Matches.objects.order_by('?').filter(user1=request.user)
    for cur_id1 in matches_user1:
        matches_user_name.append(CustomUser.objects.get(id=cur_id1.user2_id))

    matches_user2 = Matches.objects.order_by('?').filter(user2=request.user)
    for cur_id2 in matches_user2:
        matches_user_name.append(CustomUser.objects.get(id=cur_id2.user1_id))

    if matches_user_name:
        context = {'users': matches_user_name}
        return render(request, 'app/matches.html', context)
    else:
        return render(request, 'app/no_likes.html')


@login_required(login_url='login/')
def profile_edit(request):
    return render(request, 'app/profile_edit.html')
