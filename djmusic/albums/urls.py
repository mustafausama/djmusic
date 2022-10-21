from django.urls import path
from . import views

app_name = 'albums'

urlpatterns = [
  path('create/', views.create_album, name='create')
]
