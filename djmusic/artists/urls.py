from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'artists'
urlpatterns = [
  path('', views.ArtistsView.as_view(), name='json_list'),
  # path('old/create/',  login_required(views.CreateArtistView.as_view()), name='create'),
  # path('old/', views.ArtistListView.as_view(), name='list')
]
urlpatterns = format_suffix_patterns(urlpatterns)
