import factory
from artists.models import Artist

class ArtistFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Artist
  stage_name = factory.Faker('user_name')

  