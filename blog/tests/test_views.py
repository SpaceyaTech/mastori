from django.test import TestCase
from rest_framework.test import APITestCase
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
        response = self.client.get("/mastori/")
        
        self.assertEqual(response.status_code, 200)
        mastori_json = json.loads(response.content)

        # Expecting only one object, the one with 'Published' status to be returned
        self.assertEqual(len(mastori_json), 1)
        self.assertTrue(mastori_json[0]['status']=="Published")