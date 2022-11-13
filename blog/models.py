from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    display_photo = models.ImageField(upload_to="path/to/avatars/", null=True, blank=True)
    bio = models.CharField(max_length=255)


