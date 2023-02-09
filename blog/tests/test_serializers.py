
from model_bakery import baker
from rest_framework import status

from django.test import TestCase, Client
from django.urls import reverse

from blog.models import Stori
from blog.serializers import BlogSerializer


# Create your tests here.

class TestBlog(TestCase):
    def setUp(self):
        self.client = Client()
        self.obj1 = baker.make(Stori,content="This is an interesting story about amaizinng developers at space ya teck")
        self.obj2 = baker.make(Stori,content="This is an interesting story about amaizinng developers at space ya teck")
        self.obj3 = baker.make(Stori,content="This is an interesting story about amaizinng developers at space ya teck")
        
        
    def test_get_all_stori(self):
        response = self.client.get(reverse("get-all-stories"))
        stories = Stori.objects.all()
        serializer = BlogSerializer(stories,many=True) 
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
