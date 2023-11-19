from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Likes(models.Model):
    sender = models.ForeignKey(User, related_name='likes_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='likes_received', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} liked {self.receiver} at {self.timestamp}'
