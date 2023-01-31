from django.test import TestCase
from accounts.models import Account, User
from accounts.serializers import AccountDetailSerializer, UserSerializer, UserDetailsSerializer, AddAccountSerializer, UserAccountRegistrationSerializer


class TestAccountDetailSerializer(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='TeamRio',
            email = 'teamrio@space.com',
            first_name = 'Team',
            last_name = 'Rio'
            )
        self.account = Account.objects.create(
            user = self.user,
            account_name= "default",
            bio = "default statement"
        )

    def test_account_serialization(self):
        serializer = AccountDetailSerializer(instance=self.account)
        data = serializer.data
        assert data["id"] == self.account.id
        assert data["account_name"] == "default"
        assert data["bio"] == "default statement"


class TestUserSerializer(TestCase):
    def setUp(self):
        # Create a user instance
        self.user = User.objects.create(
            username='TeamRio',
            email = 'teamrio@space.com',
            first_name = 'Team',
            last_name = 'Rio',
            password = "password123",
            )
        # create first account instance
        self.account1 = Account.objects.create(
            user = self.user,
            account_name= "default1",
            bio = "default statement1",
        )
        #create second account instance
        self.account2 = Account.objects.create(
            user = self.user,
            account_name= "default2",
            bio = "default statement2"
        )

    def test_user_serialization(self):
        serializer = UserSerializer(instance=self.user)
        data = serializer.data
        assert data["id"] == self.user.id
        assert data["first_name"] == 'Team'
        assert data["last_name"] == 'Rio'
        assert data["username"] == 'TeamRio'
        assert data["email"] == 'teamrio@space.com'
        assert data["phone_number"] == None
        assert "pasword" not in data
        assert data["number_of_accounts"] == 2



class TestUserDetailsSerializer(TestCase):
    def setUp(self):
        # Create a user instance
        self.user = User.objects.create(
            username='TeamRio',
            email = 'teamrio@space.com',
            first_name = 'Team',
            last_name = 'Rio',
            phone_number =  "+254729111812",
            password = "password123",
        )

        # Create an account instance for the user
        self.account = Account.objects.create(
        user = self.user,
        account_name= "default",
        bio = "default statement",
        )

    def test_user_details_serialization(self):
        # Create an instance of the UserDetailsSerializer with the user instance
        serializer = UserDetailsSerializer(instance=self.user)
        data = serializer.data
        # Assert that the serialized data contains the expected values
        assert data["first_name"] == 'Team'
        assert data["last_name"] == 'Rio'
        assert data["username"] == 'TeamRio'
        assert data["email"] == 'teamrio@space.com'
        assert data["phone_number"] == "+254729111812"
        assert "pasword" not in data # Assert that the password is not present in the serialized data


class AddAccountSerializerTest(TestCase):
    def setUp(self):
        # create a new user
        self.user = User.objects.create_user(
            username = "TeamRio",
            email='teamrio@space.com', 
            password='testpassword'
        )
        self.data = {
            'account_name': 'default',
            'bio': 'default statement.',
        }
        self.context = {'user_id': self.user.id}

    def test_valid_data(self):
        # create an instance of the serializer with the test data and context
        serializer = AddAccountSerializer(data=self.data, context=self.context)
        # assert that the serializer is valid
        self.assertTrue(serializer.is_valid())
        # save the account instance
        account = serializer.save()
        # assert that the account's user, account_name, and bio attributes are as expected
        self.assertEqual(account.user, self.user)
        self.assertEqual(account.account_name, 'default')
        self.assertEqual(account.bio, 'default statement.')

#from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import Account
from accounts.serializers import UserAccountRegistrationSerializer
from rest_framework import serializers

class UserAccountRegistrationSerializerTestCase(APITestCase):
    def setUp(self):
        self.valid_payload = {
            'user': {
                'username': 'TeamRio',
                'first_name': 'Team',
                'last_name': 'Rio',
                'email': 'teamrio@space.com',
                'phone_number': "+254729111812",
                'password': 'password123'
            },
            'confirm_password': 'password123',
            'account_name': 'testaccount',
            'bio': 'test bio'
        }

    def test_create_valid_user_account(self):
        serializer = UserAccountRegistrationSerializer(data=self.valid_payload)
        self.assertTrue(serializer.is_valid(), msg=serializer.errors)
        user_account = serializer.save()
        self.assertIsInstance(user_account, Account)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Account.objects.count(), 1)

