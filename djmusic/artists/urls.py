from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'artists'
urlpatterns = [
  path('create/',  login_required(views.CreateArtistView.as_view()), name='create'),
  path('', views.ArtistListView.as_view(), name='list')
]
