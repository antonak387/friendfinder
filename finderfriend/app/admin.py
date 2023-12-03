from django.contrib import admin

# Register your models here.
from .models import Likes, CustomUser

admin.site.register(Likes)
admin.site.register(CustomUser)