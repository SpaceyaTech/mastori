from django.test import TestCase,Client
from django.urls import reverse
from post.models import BlogPost
import json

# Create your tests here.

class TestViews(TestCase):
    def setUp(self) -> None:
        self.client =Client()
        self.create_post=reverse('create_post')
        self.single_post=reverse('single_post')
        self.all_posts=reverse('all_posts')
        self.update_post=reverse('update_post')
        self.delete_post=reverse('delete_post')

   

    

        




