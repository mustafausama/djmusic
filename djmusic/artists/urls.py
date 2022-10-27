from django.urls import path
from . import views

app_name = 'artists'
urlpatterns = [
  # path('create/', views.create_artist, name='create'),
  path('create/', views.create_artist.as_view(), name='create'),
  path('', views.ArtistList.as_view(), name='list')
]
