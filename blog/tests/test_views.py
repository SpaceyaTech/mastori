from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import User
from blog.models import Stori, Category
import json

# Create your tests here.

# class TestStoriList(APITestCase):
    
#     def test_storilist(self):
#         self.client

class TestStoriList(TestCase):
    def setUp(self):
        self.test_category = Category.objects.create(name="Test Category")

        Stori.objects.create(title="Test 1", slug="test-1", description="Test 1", content="Story 1", category=self.test_category)
        Stori.objects.create(title="Test 2", slug="test-2", description="Test 2", content="Story 2", status="Published", category=self.test_category)

    """
    Test the /mastori/ endpoint to ascertain whether
    only published blogs are returned
    """
    def test_only_published_stori_returned(self):
        mastori_url = reverse('mastori-list')
        response = self.client.get(mastori_url)
        
        self.assertEqual(response.status_code, 200)
        mastori_json = json.loads(response.content)

        # Expecting only one object, the one with 'Published' status to be returned
        self.assertEqual(len(mastori_json), 1)
        self.assertTrue(mastori_json[0]['status']=="Published")

class TestCategoryCreation(TestCase):
    """
    Test the categories endpoint to ascertain whether
    only logged in users can create categories
    """
    def test_only_logged_in_users_create_category(self):
        test_user = User.objects.create_user(
            first_name="Zaphod", 
            last_name="Beeblebrox", 
            email="hitchhiker@local.com", 
            username="hitchhiker", 
            password="Beeblebrox42")
        
        test_data = {
            'name': 'Test Category 1'
        }

        categories_url = reverse('categories-list')
        # This is an UNAUTHORIZED post that bypasses the created user above
        response = self.client.post(categories_url, test_data)
        # Check whether the category has NOT been created
        self.assertEqual(response.status_code, 401)

        c = APIClient()
        refresh = RefreshToken.for_user(test_user)
        c.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        # This is an AUTHORIZED post that gets a token for the created user
        response = c.post(categories_url, test_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

