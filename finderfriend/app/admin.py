from django.contrib import admin

# Register your models here.
from .models import Likes, CustomUser, Matches

admin.site.register(Likes)
admin.site.register(CustomUser)
admin.site.register(Matches)
