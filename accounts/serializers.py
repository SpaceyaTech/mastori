from rest_framework import serializers
from .models import Account


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ["id", "name", "display_picture", "bio"]

    
