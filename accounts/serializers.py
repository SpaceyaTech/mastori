from rest_framework import serializers
from .models import Account, User


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ["id", "name", "display_picture", "bio"]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'verification_code', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}


