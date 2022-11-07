from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'users'
urlpatterns = [
  path('<int:pk>/', views.UserDetailView.as_view(), name='user_details'),  
]
urlpatterns = format_suffix_patterns(urlpatterns)
