import pytest
import json

@pytest.mark.django_db
def test_artists_view(auth_client, create_artists):
  artists = create_artists(10)
  client = auth_client()
  response = client.get('/artists/')
  
  assert response.status_code == 200
  assert len(json.loads(response.content)) == len(artists)
  artists_list = json.loads(response.content)
  for i in range(len(artists)):
    assert {
      'id': artists[i].id, 'stage_name': artists[i].stage_name, 'social_link': artists[i].social_link
      } in artists_list

