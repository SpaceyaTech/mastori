import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from accounts.models import Account, User
from blog.models import Stori, Category, Comment

@pytest.fixture
def api_client():
    return APIClient

@pytest.fixture
def user():
    return User.objects.create(
        username= "Teamrio",
        email= "teanrio@example.com",
        first_name= "Team",
        last_name="Rio"
    )

@pytest.fixture
def account(user):
    return Account.objects.create(
        user=user,
        account_name="teamrioaccount"
    )

@pytest.fixture
def category():
    return Category.objects.create(
        name="testdafault"
    )

@pytest.fixture
def stori(category, account):
    return Stori.objects.create(
        title= "testing",
        slug= "testing-slug",
        description= "Testing stori",
        content= "testing using pytest",
        category = category,
        created_at=account,
        status=0
    )

@pytest.mark.django_db
def test_create_comment(stori, account):
    comment = Comment.objects.create(
        Post_id= stori,
        user= account,
        body= "This is first comment"
    )

    assert Comment.objects.count() == 1
    assert comment.Post_id == stori
    assert comment.user == account
    assert comment.body == 'This is first comment'
