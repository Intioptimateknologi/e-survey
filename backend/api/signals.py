from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from api import models


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance=None, created=False, **kwargs):
#     if created:
#         print(f'-> SUCCESS: user profile for user {instance.username} was created')
#         models.profile.objects.create(
#             user=instance
#         )
