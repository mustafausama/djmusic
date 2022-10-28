from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/', include('artists.urls')),
    path('albums/', include('albums.urls')),
    path("accounts/login/", auth_views.LoginView.as_view()),
    path("accounts/logout/", auth_views.LogoutView.as_view())
]
