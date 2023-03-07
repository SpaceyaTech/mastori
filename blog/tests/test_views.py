import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from blog.models import Stori, Category
from accounts.models import Account, User
from blog.serializers import StoriViewersSerializer


@pytest.mark.django_db
def test_stori_viewers_count():
    client = APIClient()
    user= User.objects.create(username= "Teamrio", email= "teanrio@example.com",first_name= "Team", last_name="Rio")
    account = Account.objects.create(user=user, account_name="teamrioaccount")
    category= Category.objects.create(name="testdafault")
    stori = Stori.objects.create( title= "testing", slug= "testing-slug", description= "Testing stori", content= "testing number of viewer using pytest", category = category, created_at=account, status=0)
    stori.viewers.add(account)
    stori_serializer = StoriViewersSerializer(stori)

    url = reverse('stori-count', kwargs={'slug': stori.slug})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == stori_serializer.data

@pytest.mark.django_db
def test_stori_viewers_not_count():
    client = APIClient()
    user= User.objects.create(username= "Teamrio", email= "teanrio@example.com",first_name= "Team", last_name="Rio")
    account = Account.objects.create(user=user, account_name="teamrioaccount")
    category= Category.objects.create(name="testdafault")
    stori = Stori.objects.create( title= "testing", slug= "testing-slug", description= "Testing stori", content= "testing number of viewer using pytest", category = category, created_at=account, status=0)
    stori_serializer = StoriViewersSerializer(stori)

    url = reverse('stori-count', kwargs={'slug': stori.slug})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == stori_serializer.data

