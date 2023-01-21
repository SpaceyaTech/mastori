from django.test import TestCase
from accounts.models import Account, User
from accounts.serializers import AccountDetailSerializer, UserSerializer, UserDetailsSerializer

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
        self.user = User.objects.create(
            username='TeamRio',
            email = 'teamrio@space.com',
            first_name = 'Team',
            last_name = 'Rio',
            password = "password",
            )
        # first account instance
        self.account1 = Account.objects.create(
            user = self.user,
            account_name= "default1",
            bio = "default statement1",
        )
        #'second account instance
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
        self.user = User.objects.create(
            username='TeamRio',
            email = 'teamrio@space.com',
            first_name = 'Team',
            last_name = 'Rio',
            phone_number =  "+23434567890",
            password = "password",
        )

        self.account = Account.objects.create(
        user = self.user,
        account_name= "default",
        bio = "default statement",
        )

    def test_user_details_serialization(self):
        serializer = UserDetailsSerializer(instance=self.user)
        data = serializer.data
        assert data["first_name"] == 'Team'
        assert data["last_name"] == 'Rio'
        assert data["username"] == 'TeamRio'
        assert data["email"] == 'teamrio@space.com'
        assert data["phone_number"] == "+23434567890"
        assert "pasword" not in data

