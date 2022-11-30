from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings

"""
Substituting a custom User by extending the AbstractUser
Making Users email unique
Adding extra attributes that are not present in the default User model(phone_number and verification code)
USERNAME_FIELD - changing login to use email rather than username.
REQUIRED_FIELDS - the required fields to create a superuser
"""





class User(AbstractUser):
    username = models.CharField(blank=True,  max_length=10,unique=True)
    first_name= models.CharField(max_length=255,db_index=True)
    last_name= models.CharField(max_length=255, db_index=True)
    email = models.EmailField(_('email address'), unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    verification_code = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)
    
    def tokens(self):
        refresh= RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }




class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField()
    display_picture = models.ImageField(upload_to='uploads', blank=True)
    bio = models.TextField(blank=True)
