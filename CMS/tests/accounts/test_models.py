from django.test import TestCase
from accounts.models import User
# Create your tests here.

class TestUser(TestCase):
    

    def setUp(self) -> None:
        '''
        create an instance of a user and save
        '''
        user = User.objects.create(
        email = "test.user@example.com",
        phone_number = "+254909000"
        )
        user.save()

    def test_user_is_saved(self):
        '''TEst if the user is being saved'''
        self.assertEquals(len(User.objects.all()),1)


    def test_is_instance_of(self):
        '''
        confirm the user is an instance of User model
        '''
        
        user = User.objects.get(email="test.user@example.com")
        self.assertIsInstance(user,User)



   

