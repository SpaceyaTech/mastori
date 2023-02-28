from rest_framework import serializers
from django.db import transaction
from django.conf import settings

from accounts.models import User, Account


class AccountDetailSerializer(serializers.ModelSerializer):
    """Serializer to display account details to be used in the UserSerializer"""

    class Meta:
        model = Account
        fields = ['id', 'account_name', 'bio']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    number_of_accounts = serializers.IntegerField(read_only=True) #Added field to display the number of accounts that a user has.
    account = AccountDetailSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'phone_number', 
            'password', 
            'number_of_accounts', 
            'account'
        ]


class UserDetailsSerializer(serializers.ModelSerializer):
    """Serializer to display the User Details to be used on account registration"""

    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    def validate_password(self, value):
        """Validating password length"""

        password_length = settings.USER_PASSWORD_LENGTH

        if len(value) < password_length:
            raise serializers.ValidationError(
                f"Password length must be at least {password_length} characters"
            )

        return value

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password']


class UserAccountRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registration of user and first account that is created when a user is registered
    It ensures that a first user does not exist without an account.
    """

    confirm_password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    user = UserDetailsSerializer()

    def create(self, validated_data):
        user = dict(validated_data['user'])
        password = user['password']

        with transaction.atomic():
            user = User.objects.create_user(
                username=user['username'], 
                first_name=user['first_name'], 
                last_name=user['last_name'], 
                email=user['email'], 
                phone_number=user['phone_number'], 
                password=password
            )

            account = Account.objects.create(
                user=user, 
                account_name=validated_data['account_name'], 
                bio=validated_data['bio']
            )

            return account
    
    def validate(self, data):
        """
        Validating if password field data equals confirm_password field data.
        """

        user = dict(data["user"])
        password = user["password"]
        confirm_password = data["confirm_password"]

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        return data

    class Meta:
        model = Account
        fields = ['id', 'user', 'confirm_password', 'account_name', 'display_picture', 'bio']


class AddAccountSerializer(serializers.ModelSerializer):
    """Serializer that enables addition of a new account to an existing user"""

    def create(self, validated_data):
        user_id = self.context['user_id']
        account_name = validated_data['account_name']
        bio = validated_data['bio']

        user = User.objects.get(pk=user_id)

        account = Account.objects.create(user=user, account_name=account_name, bio=bio)

        return account
        
    class Meta:
        model = Account
        fields = ['id','account_name', 'bio']
