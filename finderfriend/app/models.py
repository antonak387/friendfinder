from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Likes(models.Model):
    sender = models.ForeignKey('CustomUser', related_name='likes_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey('CustomUser', related_name='likes_received', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'


class Matches(models.Model):
    user1 = models.ForeignKey('CustomUser', related_name='user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey('CustomUser', related_name='user2', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'


class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )

    gender = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.CharField('Дата рождения', default='2000-01-01')
    image = models.ImageField('Фотография профиля', upload_to='images/', blank=True, null=True)


class Message(models.Model):
    value = models.CharField(max_length=100000)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=255)
    match_id = models.IntegerField()
