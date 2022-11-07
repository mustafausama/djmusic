from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'authentication'
urlpatterns = [
  path('register/', views.RegisterView.as_view(), name='register'),
  path('login/', views.LoginView.as_view(), name='login'),
  path('logout/', views.LogoutView.as_view(), name='logout'),
  
]
urlpatterns = format_suffix_patterns(urlpatterns)
