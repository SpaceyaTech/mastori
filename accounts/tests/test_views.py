from django.test import RequestFactory, TestCase
from accounts.models import User, Account
from accounts.views import UserViewSet, AddUserAccountViewSet
from rest_framework.test import force_authenticate

class UserViewSetTestCase(TestCase):
    def setUp(self):
        # Initialize the RequestFactory
        self.factory = RequestFactory()        
        # Get the view for the UserViewSet
        self.view = UserViewSet.as_view(actions={'get': 'list'})       
        # Create a superuser for testing purposes
        self.user = User.objects.create_superuser(            
            username = "TeamRio",
            email='teamrio@space.com', 
            password='testpassword'
            )
        
    def test_user_list_with_admin_permission(self):
        # Create a GET request to retrieve the list of users
        request = self.factory.get('/users/')       
        # Authenticate the superuser for the request
        force_authenticate(request, self.user)        
        # Set the request user to the superuser
        request.user = self.user       
        # Send the request to the view
        response = self.view(request)        
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_user_list_without_admin_permission(self):
        # Create a regular user for testing purposes
        user = User.objects.create_user(
            username='regular_user', 
            password='password123', 
            email='regular_user@example.com'
            )        
        # Create a GET request to retrieve the list of users
        request = self.factory.get('/users/')       
        # Authenticate the regular user for the request
        force_authenticate(request, user=user)   
        # Send the request to the view
        response = self.view(request)       
        # Assert that the response status code is 403 (Forbidden)
        self.assertEqual(response.status_code, 403)


class AddUserAccountViewSetTestCase(TestCase):
    def setUp(self):
        # Initialize the request factory
        self.factory = RequestFactory()
        # Set the view for the test case
        self.view = AddUserAccountViewSet.as_view(actions={'post': 'create'})
        # Create a user for testing
        self.user = User.objects.create_user(
            username='TeamRio',
            first_name='Team',
            last_name='Rio',
            email='teamrio@space.com',
            phone_number="+254729111812",
            password='password123',
        )
        # Create an account for testing
        self.account = Account.objects.create(
            user=self.user,
            account_name='test_account',
            display_picture='test_image.jpg',
            bio='test_bio',
        )
    
    def test_add_user_account_with_valid_data(self):
        # Test with valid data
        request = self.factory.post("/add_account/1/", {
            "user": {
                'username': 'TeamRio',
                'first_name': 'Team',
                'last_name': 'Rio',
                'email': 'teamrio@space.com',
                'phone_number': "+254729111812",
                'password': 'password123'
            },
            "confirm_password": "password123",
            "account_name": "default",
            "bio": "default statament"
        }, format="json")

        # Force authenticate the user
        force_authenticate(request, user=self.user)
        # Call the view with user primary key (pk)
        response = self.view(request, user_pk=1)
        # Assert that the response status code is 201 (created)
        self.assertEqual(response.status_code, 201)

    def test_add_user_account_with_invalid_data(self):
        # Test with invalid data
        request = self.factory.post("/add_account/1/", {
            "user": {
                'username': '',
                'first_name': '',
                'last_name': '',
                'email': '',
                'phone_number': "",
                'password': ''
            },
            "confirm_password": "",
            "account_name": "",
            "bio": ""
        }, format="json")

        # Force authenticate the user
        force_authenticate(request, user=self.user)
        # Call the view with user primary key (pk)
        response = self.view(request, user_pk=1)
        # Assert that the response status code is 400 (bad request)
        self.assertEqual(response.status_code, 400)
