from django.db import models

from django.contrib.auth.models import User, AbstractUser, Group
from PIL import Image
from django.core.exceptions import ObjectDoesNotExist

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nik  = models.CharField(max_length=16, null=True, blank=True)
    phone  = models.CharField(max_length=20, null=True, blank=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    avatar = models.ImageField(default='images/avatar.png', upload_to='avatars')
    # role = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')

    visible_password = models.TextField(max_length=255, verbose_name='visible_password', blank=True, null=True)

    deleted_at = models.DateTimeField(auto_now_add=False, editable=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Profile User'
        verbose_name_plural = 'Daftar Profile User'
        db_table = 'auth_user_profile'

    def __str__(self):
        return f'{self.user.username} - profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
