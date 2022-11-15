import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phone_field import PhoneField

class CustomUserManager(BaseUserManager):

    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def createUser(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.'")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_staff=True.'")

        return self.createUser(email=email, password=password, **extra_fields)


# Create a custom user model using AbstractBaseUser subclass
# PermissionsMixin makes it easy to include django's permissions into user class

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    #verifcation_code = models.CharField(max_length=1000) handle this by creating a function later
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    
    objects = CustomUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username', 'phone_number']

    def __str__(self):
        return self.username



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    display_photo = models.ImageField(null=True, blank=True)
    bio = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name



