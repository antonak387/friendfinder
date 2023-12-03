from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Likes(models.Model):
    sender = models.ForeignKey('CustomUser', related_name='likes_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey('CustomUser', related_name='likes_received', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )

    gender = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.CharField('Дата рождения', default='2000-01-01')
