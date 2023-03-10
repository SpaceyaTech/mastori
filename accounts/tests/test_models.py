from django.test import TestCase
from  ..models import User, Account
from django.utils import timezone
import time
import string
# Create your tests here.


#Tests verification code
class UserVerificationCodeTestCase(TestCase):
    def test_verification_code(self):
               
        user = User.objects.create(email='spaceyatech@example.com')        
       
        initial_code = user.verification_code            
        self.assertEqual(len(str(initial_code)), 6)        
        
        user.code_generated_at = timezone.now() - timezone.timedelta(hours=1)
        user.save()        
        
        updated_code = user.get_verification_code()
        self.assertNotEqual(initial_code, updated_code)
        print(f' Initial code is {initial_code} vs updated code is {updated_code}')     
    
        user.code_generated_at = timezone.now() - timezone.timedelta(minutes=59)
        user.save()        
      
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