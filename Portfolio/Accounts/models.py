from django.db import models
from django.forms import TextInput, EmailInput
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='media/profile_pictures/', null=True, blank=True)
    bio = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    account = models.Manager()

