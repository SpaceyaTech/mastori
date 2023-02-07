from django.test import TestCase
from  ..models import User, Account
from django.utils import timezone
import time
import string
# Create your tests here.


class UserVerificationCodeTestCase(TestCase):
    def test_verification_code(self):
        # Create a user        
        user = User.objects.create(email='test@example.com')
        
        # Check that the initial verification code is generated correctly
        initial_code = user.verification_code            
        self.assertEqual(len(str(initial_code)), 6)
        
        # Update the code_generated_at time to be an hour ago
        user.code_generated_at = timezone.now() - timezone.timedelta(hours=1)
        user.save()
        
        # Check that the verification code is updated after an hour has passed
        updated_code = user.get_verification_code()
        self.assertNotEqual(initial_code, updated_code)
        
        # Update the code_generated_at time to be less than an hour ago
        user.code_generated_at = timezone.now() - timezone.timedelta(minutes=59)
        user.save()
        
        # Check that the verification code is not updated if less than an hour has passed
        same_code = user.get_verification_code()
        self.assertEqual(updated_code, same_code)


class UserTestCase(TestCase):
    def test_create_user(self):
        user  = User.objects.create(username='TeamRio',email = 'teamrio@space.com',first_name = 'Team',last_name = 'Rio')
        user.set_password('password12!')
        user.save()
        
        self.assertEqual(str(user),'Team Rio')


class AccountTestCase(TestCase):
    
    def test_account_create(self):
        user  = User.objects.create(username='TeamRio',email = 'teamrio@space.com',first_name = 'Team',last_name = 'Rio')
        account = Account.objects.create (user=user, account_name = 'space')
        account.save()
        
        self.assertEqual(str(account),"space")