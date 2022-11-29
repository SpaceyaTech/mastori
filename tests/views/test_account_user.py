from django.urls import path, reverse, include, resolve
from django.test import SimpleTestCase
from accounts.views import AccountAllView, UserAllView
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from accounts.models import User



class AccountUrlsTests(SimpleTestCase):

    def test_get_accounts_is_resolved(self):
        url = reverse('account')
        self.assertEquals(resolve(url).func.view_class, AccountAllView)

class UserUrlsTests(SimpleTestCase):

    def test_get_users_is_resolved(self):
        url = reverse('user')
        self.assertEquals(resolve(url).func.view_class, UserAllView)


class UserAPIViewTests(APITestCase):
    users_url = reverse("user")
    users_create_url = reverse("create-user")

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='some-strong-password')
        self.token = Token.objects.create(user=self.user)
        #self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def tearDown(self):
        pass

    def test_get_users_authenticated(self):
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_users_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.users_url)
        self.assertEquals(response.status_code, 401)


    def test_post_customer_authenticated(self):
        data = {
            "email": "messi0909@example.com",
            "first_name": "Tayo",
            "last_name": "Mesyoo",
            "verification_code": "298",
            "phone_number": "000010101"
        }
        response = self.client.post(self.users_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'],"Tayo")
        self.assertEqual(len(response.data), 6)


class UserDetailAPIViewTests(APITestCase):
    user_url = reverse("user-detail", args=[1])
    users_url = reverse("user")
    users_create_url = reverse("create-user")

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='some-strong-password')
        self.token = Token.objects.create(user=self.user)
        #self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


        data = {
            "email": "messi0909@example.com",
            "first_name": "Brucc",
            "last_name": "Lee",
            "verification_code": "298",
            "phone_number": "000010101",
        }
        response = self.client.post(self.users_create_url, data, format='json')

    def test_get_user_autheticated(self):
        response = self.client.get(self.user_url )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['last_name'], 'Lee')
        
    def test_get_user_unautheticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.user_url )
        self.assertEqual(response.status_code, 401)

    def test_delete_user_authenticated(self):
        response = self.client.delete(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class AccountAPIViewTests(APITestCase):
    accounts_url = reverse("account")

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='some-strong-password')
        self.token = Token.objects.create(user=self.user)
        #self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def tearDown(self):
        pass

    def test_get_accounts_authenticated(self):
        response = self.client.get(self.accounts_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_accounts_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.accounts_url)
        self.assertEquals(response.status_code, 401)