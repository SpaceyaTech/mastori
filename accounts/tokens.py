from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


def auth_token(user: User):
    refresh = RefreshToken.for_user(user)

    tokens = {"access": str(refresh.access_token), "refresh": str(refresh)}

    return tokens
