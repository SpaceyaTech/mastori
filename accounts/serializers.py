from django.db import transaction
from djoser.serializers import UserSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from accounts.models import Account, User


class AccountDetailsSerializer(serializers.ModelSerializer):
    """Account details to be used when creating a user"""

    class Meta:
        model = Account
        fields = ['bio', 'display_picture']


class UserAccountRegistrationSerializer(UserSerializer):
    """
    Serializer for registration of user and first account that is created when a user is registered
    It ensures that a first user does not exist without an account.
    """
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    confirm_password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    account = AccountDetailsSerializer(required=False)

    def create(self, validated_data):
        if validated_data.get("account") is not None:
            account = dict(validated_data["account"])
        else:
            account = {}
        
        with transaction.atomic():
            user = User.objects.create_user(
                username=validated_data['username'], 
                first_name=validated_data['first_name'], 
                last_name=validated_data['last_name'], 
                email=validated_data['email'], 
                phone_number=validated_data.get("phone_number"), 
                password=validated_data['password']
            )
                
            account = Account.objects.create(
                user=user, 
                account_name=validated_data['username'], 
                bio=account.get("bio")
            )

            return user
            
    
    def validate(self, data):
        """
        Validating if password field data equals confirm_password field data.
        """

        password = data["password"]
        confirm_password = data["confirm_password"]

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        return data


    class Meta:
        model = User
        fields = ['id', 'account', 'first_name', 'last_name', 'username', 'email', 'phone_number', 'password', 'confirm_password']


class CustomUserSerializer(UserSerializer):
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "phone_number"]
