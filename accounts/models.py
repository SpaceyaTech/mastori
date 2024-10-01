import secrets
import string
import time
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

_VERIFICATION_CODE_RANGE: range = range(4, 7)


def _generate_verification_code(size: int = 6) -> str:
    """
    Securely generates a random code in valid range.

    Note:
        This util is currently coupled to the `secrets` library.
        Changes may result in failing tests.
    """
    if size not in _VERIFICATION_CODE_RANGE:
        errmsg = "Attempt to generate code outside of required range."
        raise ValueError(errmsg)
    sequence = string.digits
    return "".join(secrets.choice(sequence) for _ in range(size))


class User(AbstractUser):
    """
    Substituting a custom `User` by extending the `AbstractUser`.

    Note:
        Make `User` email unique.
        Add extra attributes not present in the default `User` model:
            - phone_number
            - verification code
            - code_generated_at
            - is_verified
        USERNAME_FIELD - change login to use email rather than username.
        REQUIRED_FIELDS - fields required to create a superuser.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=50)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = PhoneNumberField(
        blank=True, help_text="Contact phone number", null=True, unique=True
    )
    verification_code = models.CharField(
        max_length=6, unique=True, default=_generate_verification_code()
    )
    code_generated_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(
        default=False
    )  # to be set up later in views to change if user verified

    USERNAME_FIELD = "email"

    # add phone number as a requirement while signing up
    REQUIRED_FIELDS = ["first_name", "last_name", "username", "phone_number"]

    def __init__(self, *args, region=None, **kwargs):
        """
        The function takes in a region and then sets the region to the region
        that was passed in when the user is created
        """
        super().__init__(*args, **kwargs)
        self.region = region

    # resets the verification code after every 1hr
    def get_verification_code(self):
        now = time.time()
        elapsed = now - self.code_generated_at.timestamp()
        if elapsed > 3600:
            self.verification_code = _generate_verification_code()
            self.code_generated_at = now
            self.save
        return self.verification_code

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Referencing the customized user
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="account"
    )
    account_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    display_picture = models.ImageField(
        default="blank-profile-picture.png", upload_to="profile_images"
    )
    bio = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.account_name
