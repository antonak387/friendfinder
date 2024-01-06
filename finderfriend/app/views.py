from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Likes, Matches, Message

from django.db import connection

from datetime import datetime


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
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT *
            FROM app_customuser
            WHERE id <> %s
            ORDER BY RANDOM()
            LIMIT 1
            ''',
            [request.user.id]
        )
        row = cursor.fetchone()

    if row:
        random_user = CustomUser.objects.get(id=row[0])
        context = {'user': random_user}
        return render(request, 'app/index.html', context)
    else:
        # Handle the case when no random user is found
        return HttpResponse('No random user found.')
    

@login_required(login_url='login/')
def like_user(request, user_id):
    if request.method == 'POST':
        sender = request.user.id  # Используем user.id, чтобы получить только идентификатор пользователя
        receiver = get_object_or_404(CustomUser, id=user_id)

        with connection.cursor() as cursor:
            cursor.execute(
                '''
                INSERT INTO app_likes (sender_id, receiver_id)
                VALUES (%s, %s)
                ON CONFLICT (sender_id, receiver_id) DO NOTHING
                RETURNING 1
                ''',
                [sender, receiver.id]
            )

            row = cursor.fetchone()

            if row:
                try:
                    cursor.execute(
                        '''
                        INSERT INTO app_matches (user2_id, user1_id)
                        VALUES (%s, %s)
                        ON CONFLICT (user2_id, user1_id) DO NOTHING
                        RETURNING 1
                        ''',
                        [sender, receiver.id]
                    )
                except Exception as e:
                    # Если возникает ошибка из-за отсутствия уникального ограничения в app_matches,
                    # попробуйте другой подход, например, через проверку существования
                    pass
                else:
                    return JsonResponse({'success': True})

    return JsonResponse({'success': False})


@login_required(login_url='login/')
def profile_view(request):
    return render(request, 'app/profile.html')


@login_required(login_url='login/')
def likes(request):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT sender_id
            FROM app_likes
            WHERE receiver_id = %s
            ORDER BY RANDOM()
            LIMIT 1
            ''',
            [request.user.id]
        )

        row = cursor.fetchone()

    if row is not None:
        sender_id = row[0]

        if sender_id != request.user.id:
            like_user_name = CustomUser.objects.get(id=sender_id)
            context = {'user': like_user_name}
            return render(request, 'app/likes.html', context)
        else:
            context = {'user': -1}
            return render(request, 'app/likes.html', context)
    else:
        return render(request, 'app/no_likes.html')


@login_required(login_url='login/')
def matches(request):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT user2_id, id
            FROM app_matches
            WHERE user1_id = %s
            UNION
            SELECT user1_id, id
            FROM app_matches
            WHERE user2_id = %s
            ''',
            [request.user.id, request.user.id]
        )

        rows = cursor.fetchall()

    matches_user_name = []
    match = []

    for row in rows:
        user_id = row[0]
        match_id = row[1]

        matches_user_name.append(CustomUser.objects.get(id=user_id))
        match.append(match_id)

    if matches_user_name:
        users_and_matches = zip(matches_user_name, match)
        context = {'users_and_matches': users_and_matches}
        return render(request, 'app/matches.html', context)
    else:
        return render(request, 'app/no_likes.html')


@login_required(login_url='login/')
def chat(request, match_id):
    if match_id:
        context = {'match_id': match_id,
                   'username': request.user.username}
        return render(request, 'app/chat.html', context)
    else:
        return render(request, 'app/no_likes.html')


@login_required(login_url='login/')
def send(request):
    if request.method == 'POST':
        message_value = request.POST['message']
        username = request.POST['username']
        match_id = request.POST['match_id']
        current_timestamp = datetime.now()

        with connection.cursor() as cursor:
            cursor.execute(
                '''
                INSERT INTO app_message (value, "user", match_id, timestamp)
                VALUES (%s, %s, %s, %s)
                ''',
                [message_value, username, match_id, current_timestamp]
            )

        return HttpResponse('Message sent successfully')


@login_required(login_url='login/')
def getMessages(request, match_id):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT id, value, timestamp, "user" 
            FROM app_message 
            WHERE match_id = %s
            ORDER BY timestamp
            ''',
            [match_id]
        )

        rows = cursor.fetchall()

    messages = [{'id': row[0], 'value': row[1], 'timestamp': row[2], 'user': row[3]} for row in rows]

    return JsonResponse({"messages": messages})


@login_required(login_url='login/')
def profile_edit(request):
    return render(request, 'app/profile_edit.html')


@login_required(login_url='login/')
def interests(request):
    return render(request, 'app/interests.html')


@login_required(login_url='login/')
def beer_club(request):
    pass


@login_required(login_url='login/')
def coffee_club(request):
    pass


@login_required(login_url='login/')
def walks_club(request):
    pass


@login_required(login_url='login/')
def games_club(request):
    pass
