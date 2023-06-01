import pytest
import json
from users.models import User

@pytest.mark.django_db
def test_user_register_with_insufficient_fields(auth_client):
  client = auth_client()
  response = client.post('/authentication/register/')
  assert response.status_code == 400
  assert 'This field is required.' in json.loads(response.content)['username']
  assert 'This field is required.' in json.loads(response.content)['password1']
  assert 'This field is required.' in json.loads(response.content)['password2']

@pytest.mark.django_db
def test_user_register_with_invalid_details(auth_client, create_users):
  user = create_users(1)[0]
  client = auth_client()
  response = client.post('/authentication/register/', {'username': user.username, 'email': user.email, 'password1': 'weak'})
  assert response.status_code == 400
  assert 'This field must be unique.' in json.loads(response.content)['username']
  assert 'This field must be unique.' in json.loads(response.content)['email']
  assert 'This password is too short. It must contain at least 8 characters.' in json.loads(response.content)['password1']
    
@pytest.mark.django_db
def test_user_register_with_no_second_password(auth_client):
  client = auth_client()
  response = client.post('/authentication/register/', {'username': 'user123456', 'email': 'email@example.com', 'password1': 'Strong123Pass'})
  assert response.status_code == 400
  assert 'This field is required.' in json.loads(response.content)['password2']
    
@pytest.mark.django_db
def test_user_register_with_no_matching_password(auth_client):
  client = auth_client()
  response = client.post('/authentication/register/', {'username': 'user123456', 'email': 'email@example.com', 'password1': 'Strong123Pass', 'password2': 'different'})
  assert response.status_code == 400
  assert 'Password fields do not match' in json.loads(response.content)['password2']

@pytest.mark.django_db
def test_user_register_correctly(auth_client):
  client = auth_client()
  response = client.post('/authentication/register/', {'username': 'user123456', 'email': 'email@example.com', 'password1': 'Strong123Pass', 'password2': 'Strong123Pass'})
  assert response.status_code == 201
  assert json.loads(response.content) == {
    'username': 'user123456',
    'email': 'email@example.com'
  }

@pytest.mark.django_db
def test_user_login_incomplete_credentials(auth_client):
  client = auth_client()
  response = client.post('/authentication/login/')
  assert response.status_code == 400
  assert 'This field is required.' in json.loads(response.content)['username']
  assert 'This field is required.' in json.loads(response.content)['password']


@pytest.mark.django_db
def test_user_login_invalid_credentials(auth_client):
  username = 'user1234'
  password = 'Strong1234Pass'
  client = auth_client()
  response = client.post('/authentication/login/', {'username': username, 'password': password})
  assert response.status_code == 400
  assert 'Unable to log in with provided credentials.' in json.loads(response.content)['non_field_errors']

@pytest.mark.django_db
def test_user_login_correctly(auth_client):
  username = 'user1234'
  password = 'Strong1234Pass'
  user = User.objects.create_user(username=username, password=password)
  client = auth_client()
  response = client.post('/authentication/login/', {'username': username, 'password': password})
  assert response.status_code == 200
  assert type(json.loads(response.content)['token']) == str
  assert json.loads(response.content)['user'] == {
    'id': user.id,
    'username': user.username,
    'email': user.email,
    'bio': user.bio
  }
  
@pytest.mark.django_db
def test_user_logout_incomplete(auth_client):
  client = auth_client()
  response = client.post('/authentication/logout/')
  assert response.status_code == 401
  assert json.loads(response.content)['detail'] == "Authentication credentials were not provided."
  
@pytest.mark.django_db
def test_user_logout_correctly(auth_client, create_users):
  user = create_users(1)[0]
  client = auth_client(user)
  response = client.post('/authentication/logout/')
  assert response.status_code == 204
