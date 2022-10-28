import email
from email.policy import default
import uuid
from django.db import models
from django.forms import PasswordInput

# Create your models here.


class Author(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    unique_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=20)# with password management, we will deal with validation later 
    phonenumber = models.CharField(max_length=20, blank=False) # make a way of validating different phone numbers globally
    #display_picture = models.ImageField(upload_to='', height='', width_field='',default='')# it needs pillow if we go by the picture but if image url will only need a url of the specified image
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_created = models.DateTimeField()
    active = models.BooleanField(default=True)
    #verification_code = 
    #role_id =
    about = models.TextField()

    def __str__(self) -> str:
        return self.username