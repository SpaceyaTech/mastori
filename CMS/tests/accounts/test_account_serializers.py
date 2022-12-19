import pytest
from model_bakery import baker
from rest_framework import status


from accounts.models import *

@pytest.fixture
def create_account(api_client):
    def create(account):
        return api_client.post("/register/", account, format='json')
    return create

@pytest.fixture
def update_account(api_client):
    def update(account):
        account_sample = baker.make(Account)
        return api_client.patch(f'/users/{account_sample.user.id}/add_account/{account_sample.id}/', account)
    return update


@pytest.fixture
def delete_account(api_client):
    def delete():
        account_sample = baker.make(Account)
        return api_client.delete(f'/users/{account_sample.user.id}/add_account/{account_sample.id}/')
    return delete


@pytest.mark.django_db
class TestCreateAccount():

    def test_data_is_invalid_return_400(self, authenticate_user, create_account):
        authenticate_user()
        
        account = {
            "user": {
                "username": "Hellen",
                "first_name": "Hellen",
                "last_name": "Wain",
                "email": "",
                "phone_number" : "",
                "password": "password"
            },
            "confirm_password": "password",
            "account_name": "",
            "bio": "sdrtfgvybhj"
        }

        response = create_account(account)

        assert response.status_code == status.HTTP_400_BAD_REQUEST




@pytest.mark.django_db
class TestUpdateAccount():
    def test_if_is_authenticated_return_200(self, authenticate_user, update_account):
        authenticate_user()

        user = baker.make(User)

        account = {
            "user": user.id,
            "account_name": "Politics",
            "bio": "sdrtfgvybhj"
        }

        response = update_account(account)

        assert response.status_code == status.HTTP_200_OK

    def test_if_is_not_authenticated_return_401(self, authenticate_user, update_account):
        user = baker.make(User)

        account = {
            "user": user.id,
            "account_name": "Politics",
            "bio": "sdrtfgvybhj"
        }

        response = update_account(account)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_data_is_invalid_return_400(self, authenticate_user, update_account):
        authenticate_user()

        user = baker.make(User)

        account = {
            "user": user.id,
            "account_name": "",
            "bio": ""
        }

        response = update_account(account)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
class TestDeleteAccount():
    def test_if_is_admin_return_200(self, delete_account, authenticate_user):
        authenticate_user()

        response = delete_account()

        assert response.status_code == status.HTTP_204_NO_CONTENT


    def test_if_user_is_authenticated_return_204(self, delete_account, authenticate_user):
        authenticate_user()

        response = delete_account()

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_user_is_not_authenticated_return_401(self, delete_account):

        response = delete_account()

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

