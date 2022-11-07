from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/', include('artists.urls')),
    path('albums/', include('albums.urls')),
    path('authentication/', include('authentication.urls')),
    path('users/', include('users.urls')),
    # path("accounts/login/", auth_views.LoginView.as_view(), name='login'),
    # path("accounts/logout/", auth_views.LogoutView.as_view(), name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
