from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile


class PostAdmin(admin.ModelAdmin):
    list_display = ('created_on')


admin.site.register(Profile)