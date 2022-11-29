from django.urls import path, reverse, include, resolve
from django.test import SimpleTestCase
from accounts.views import AccountAllView, UserAllView
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from accounts.models import Account
#from rest_framework.views import APIView, RetrieveUpdateDestroyAPIView


class AccountUrlsTests(SimpleTestCase):

    def test_get_accounts_is_resolved(self):
        url = reverse('account')
        self.assertEquals(resolve(url).func.view_class, AccountAllView)

class UserUrlsTests(SimpleTestCase):

    def test_get_users_is_resolved(self):
        url = reverse('user')
        self.assertEquals(resolve(url).func.view_class, UserAllView)


class AccountAPIViewTests(APITestCase):
    accounts_url = reverse("create-account")

    def setUp(self):
        self.user = Account.objects.create_user(
            username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        #self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_accounts_authenticated(self):
        response = self.client.get(self.accounts_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)