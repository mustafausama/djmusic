from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'albums'

urlpatterns = [
  # path('create/', login_required(views.CreateAlbumView.as_view()), name='create')
]
