import pytest
from rest_framework.test import APIClient
from .test_factories import ArtistFactory

@pytest.fixture
def auth_client():
  def make_client(user = None):
    client = APIClient()
    if user:
      client.force_authenticate(user)
    return client
  return make_client

@pytest.fixture
def create_artists():
  def batch_create(n = 3):
    return ArtistFactory.create_batch(n)
  return batch_create
