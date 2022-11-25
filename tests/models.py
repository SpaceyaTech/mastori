from django.test import TestCase
from  accounts.models import User, Account

# Create your tests here.

class UserTestCase(TestCase):
    def test_create_user(self):
        user  = User.objects.create(username='TeamRio', email = 'teamrio@space.com', password = 'password12!', first_name = 'Team',last_name = 'Rio')
        self.assertEqual(str(user),'Team Rio')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'teamrio@space.com')


class AccountTestCase(TestCase):
    
    def test_account_create(self):
        user  = User.objects.create(username='TeamRio', email = 'teamrio@space.com', first_name = 'Team', last_name = 'Rio')
        account = Account.objects.create (user=user, name = 'space')
        self.assertEqual(str(account),"space")
        self.assertIsInstance(account, Account)