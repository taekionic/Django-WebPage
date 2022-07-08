from django.db.models.signals import post_save
from django.dispatch import reciever

from .models import User, Profile

@reciever(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

