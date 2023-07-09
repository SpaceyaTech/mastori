from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

import random
import time
import uuid
"""
Substituting a custom User by extending the AbstractUser
Making Users email unique
Adding extra attributes that are not present in the default User model(phone_number and verification code)
USERNAME_FIELD - changing login to use email rather than username.
REQUIRED_FIELDS - the required fields to create a superuser
"""

# Generate six digit random code
def generate_verification_code(size=6): 
    return ''.join(str(random.randint(0,9)) for i in range(size))
    

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=50)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = PhoneNumberField(blank=True, help_text='Contact phone number', null=True, unique= True)
    verification_code = models.CharField(max_length=6, unique=True,default=generate_verification_code())
    code_generated_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False) # to be set up later in views to change if user verified
    
    USERNAME_FIELD = 'email'
    
    # add phone number as a requirement while signing up
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'phone_number']

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __init__(self, *args, region=None, **kwargs):
        """  
          The function takes in a region and then sets the region to the region that was passed in when the user is created
         """
        super().__init__(*args, **kwargs)
        self.region = region
    
    
    # resets the verification code after every 1hr
    def get_verification_code(self):
        now = time.time()
        elapsed = now - self.code_generated_at.timestamp()
        if elapsed > 3600: 
            self.verification_code = generate_verification_code()
            self.code_generated_at = now
            self.save
        return self.verification_code
    

class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Referencing the customized user
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='account')
    account_name = models.CharField(max_length=50, unique= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    display_picture = models.ImageField(default='blank-profile-picture.png', upload_to='profile_images')
    bio = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.account_name


