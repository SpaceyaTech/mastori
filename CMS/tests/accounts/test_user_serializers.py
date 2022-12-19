import pytest
from rest_framework import status
from model_bakery import baker

from accounts.models import User

@pytest.mark.django_db
class TestGetUsers():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        response = api_client.get("/users/")

        assert response.status_code == status.HTTP_200_OK

    def test_if_is_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        response = api_client.get("/users/")

        assert response.status_code == status.HTTP_403_FORBIDDEN

    

@pytest.mark.django_db
class TestGetUserById():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        user = baker.make(User)

        response = api_client.get(f"/users/{user.id}/")

        assert response.status_code == status.HTTP_200_OK

    def test_if_is_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        user = baker.make(User)

        response = api_client.get(f"/users/{user.id}/")

        assert response.status_code == status.HTTP_403_FORBIDDEN

    

    def test_if_user_exists(self, authenticate_user, api_client):
        authenticate_user()

        user = baker.make(User)

        response = api_client.get(f"/users/{user.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "email": user.email,
            "phone_number": user.phone_number,
            "account": [],
            "number_of_accounts": 0
        }