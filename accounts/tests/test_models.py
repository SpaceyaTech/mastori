from django.test import TestCase
from  accounts.models import User, Account
from django.contrib.auth import get_user
from  ..models import User, Account


# Create your tests here.

class UserTestCase(TestCase):
    def test_create_user(self):
        user  = User.objects.create(username='TeamRio',email = 'teamrio@space.com',first_name = 'Team',last_name = 'Rio')
        user.set_password('password12!')
        user.save()
        
        self.assertEqual(str(user.first_name+' '+user.last_name),'Team Rio')


class AccountTestCase(TestCase):
    
    def test_account_create(self):
        user  = User.objects.create(username='TeamRio',email = 'teamrio@space.com',first_name = 'Team',last_name = 'Rio')
        account = Account.objects.create (user=user, name = 'space')
        account.save()
        
        self.assertEqual(str(account.name),"space")

