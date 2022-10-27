from django.urls import path
from . import views

app_name = 'albums'

urlpatterns = [
  path('create/', views.create_album.as_view(), name='create')
]
