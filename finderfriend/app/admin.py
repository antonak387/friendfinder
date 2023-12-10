from django.contrib import admin
from .models import Likes, CustomUser, Matches, Message

admin.site.register(CustomUser)
admin.site.register(Likes)
admin.site.register(Matches)
admin.site.register(Message)
