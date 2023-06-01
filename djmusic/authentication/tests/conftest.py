import pytest
from rest_framework.test import APIClient
from .test_factories import UserFactory

@pytest.fixture
def auth_client():
  def make_client(user = None):
    client = APIClient()
    if user:
      client.force_authenticate(user)
    return client
  return make_client

@pytest.fixture
def create_users():
  def batch_create(n = 3):
    return UserFactory.create_batch(n)
  return batch_create
