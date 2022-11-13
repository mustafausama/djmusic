import factory
from ..models import User

class UserFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = User
  username = factory.Faker('user_name')
  email = factory.Faker('email')
  bio = factory.Faker('paragraph', nb_sentences=2)


  