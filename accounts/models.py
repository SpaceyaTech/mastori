from django.db import models
from django.contrib.auth.models import AbstractUser

"""
Substituting a custom User by extending the AbstractUser
Making Users email unique
Adding extra attributes that are not present in the default User model(phone_number and verification code)
USERNAME_FIELD - changing login to use email rather than username.
REQUIRED_FIELDS - the required fields to create a superuser
"""
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=50)
    phone_number = models.CharField(max_length=30, blank=True)
    verification_code = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)#Referencing the customized user
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    display_picture = models.ImageField()
    bio = models.TextField()

    def __str__(self) -> str:
        return self.name