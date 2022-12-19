from rest_framework import serializers
from django.db import transaction

from accounts.models import User, Account

"""Serializer to display account details to be used in the UserSerializer"""
class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name', 'bio']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    number_of_accounts = serializers.IntegerField(read_only=True) #Added field to display the number of accounts that a user has.
    account = AccountDetailSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'phone_number', 'password', 'number_of_accounts', 'account']

"""Serializer to display the User Details to be used on account registration"""
class UserDetailsSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password']


"""
Serializer for registration of user and first account that is created when a user is registered
It ensures that a first user does not exist without an account.
"""
class UserAccountRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    user = UserDetailsSerializer()

    def create(self, validated_data):
        user = dict(self.validated_data['user'])
        password = user['password']
        confirm_password = self.validated_data['confirm_password']

        if password == confirm_password:
            with transaction.atomic():
                user = User.objects.create_user(username=user['username'], first_name=user['first_name'], last_name=user['last_name'], email=user['email'], phone_number=user['phone_number'], password=password)

                account = Account.objects.create(user=user, account_name=self.validated_data['account_name'], bio=self.validated_data['bio'])

                return account
                
    class Meta:
        model = Account
        fields = ['id', 'user', 'confirm_password', 'account_name', 'display_picture', 'bio']


"""Serializer that enables addition of a new account to an existing user"""
class AddAccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user_id = self.context['user_id']
        account_name = self.validated_data['account_name']
        bio = self.validated_data['bio']

        user = User.objects.get(pk=user_id)

        account = Account.objects.create(user=user, account_name=account_name, bio=bio)

        return account
    class Meta:
        model = Account
        fields = ['id','account_name', 'bio']
