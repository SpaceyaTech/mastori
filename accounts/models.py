from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
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
    email = models.EmailField(unique=True, max_length=50)
    phone_number = PhoneNumberField(blank=True, help_text='Contact phone number', null=True)
    verification_code = models.CharField(max_length=100, blank=True)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'phone_number'] # add phone number as a requirement while signing up

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __init__(self, *args, region=None, **kwargs):
        """
        The function takes in a region and then sets the region to the region that was passed in when the user is created
        """
        super().__init__(*args, **kwargs)
        self.region = region
    def __str__(self):
        return "{}".format(self.email)

    def tokens(self):
        refresh= RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    
  
class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)#Referencing the customized user
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    display_picture = models.ImageField(default='blank-profile-picture.png', upload_to='profile_images')
    bio = models.TextField(blank=True, null=True)
