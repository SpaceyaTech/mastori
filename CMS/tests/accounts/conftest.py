import pytest
from rest_framework.test import APIClient

from accounts.models import User

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate_user(api_client):
    def authenticate(is_staff=True):
        return api_client.force_authenticate(user=User(is_staff=is_staff))
    return authenticate