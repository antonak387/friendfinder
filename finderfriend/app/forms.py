from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'gender', 'birth_date', 'image')
        widgets = {
            'birth_date': forms.DateInput(format='%d.%m.%y')
        }
    image = forms.ImageField(label='Фотография профиля', required=False)



