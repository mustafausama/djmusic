import pytest
import json
from urllib.parse import urlencode  

@pytest.mark.django_db
def test_unauthenticated_user_view(auth_client, create_users):
  user = create_users(1)[0]
  client = auth_client()
  response = client.get(f'/users/{user.id}/')
  assert response.status_code == 200
  assert json.loads(response.content) == {
    'id': user.id,
    'username': user.username,
    'email': user.email,
    'bio': user.bio
  }
  
@pytest.mark.django_db
def test_unauthorized_user_update(auth_client, create_users):
  [user1, user2] = create_users(2)
  guest = auth_client()
  client1 = auth_client(user1)
  guest_response = guest.patch(f'/users/{user2.id}/', urlencode({'username': 'user2'}), content_type='application/x-www-form-urlencoded')
  assert guest_response.status_code == 401
  assert json.loads(guest_response.content)['detail'] == "Authentication credentials were not provided."
  
  client1_response = client1.patch(f'/users/{user2.id}/', urlencode({'username': 'user2'}), content_type='application/x-www-form-urlencoded')  
  assert client1_response.status_code == 403
  assert json.loads(client1_response.content)['detail'] == "You do not have permission to perform this action."

@pytest.mark.django_db
def test_authorized_user_update(auth_client, create_users):
  user = create_users(1)[0]
  client = auth_client(user)
  response = client.patch(f'/users/{user.id}/', urlencode({'username': 'user'}), content_type='application/x-www-form-urlencoded')
  assert response.status_code == 200
  assert json.loads(response.content)['username'] == 'user'

@pytest.mark.django_db
def test_invalid_user_update(auth_client, create_users):
  user = create_users(1)[0]
  client = auth_client(user)
  response = client.patch(f'/users/{user.id}/', urlencode({'email': 'new.email'}), content_type='application/x-www-form-urlencoded')
  assert response.status_code == 400
  assert 'Enter a valid email address.' in json.loads(response.content)['email']


@pytest.mark.django_db
def test_incomplete_user_update(auth_client, create_users):
  user = create_users(1)[0]
  client = auth_client(user)
  response = client.put(f'/users/{user.id}/', urlencode({'email': 'new.email@example.com'}), content_type='application/x-www-form-urlencoded')
  assert response.status_code == 400
  assert 'This field is required.' in json.loads(response.content)['username']

