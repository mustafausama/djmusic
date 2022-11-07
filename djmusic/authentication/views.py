from rest_framework import generics
from rest_framework import permissions
from .serializers import RegisterSerializer
from users.serializers import UserSerializer
from knox.views import LoginView as KnoxLoginView, LogoutView as KnoxLogoutView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login

class RegisterView(generics.CreateAPIView):
  permission_classes = [permissions.AllowAny]
  serializer_class = RegisterSerializer

class LoginView(KnoxLoginView):
  permission_classes = (permissions.AllowAny,)
  
  def post(self, request, format=None):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    login(request, user)
    return super(LoginView, self).post(request, format=None)
  
  def get_post_response_data(self, request, token, instance):
    UserSerializer = self.get_user_serializer_class()
    
    data = {
      'token': token
    }
    print(UserSerializer)
    if UserSerializer is not None:
      data['user'] = UserSerializer(request.user, context=self.get_context()).data
    return data

  def get_user_serializer_class(self):
    return UserSerializer

class LogoutView(KnoxLogoutView):
  pass