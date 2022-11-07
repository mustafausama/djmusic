from rest_framework import generics
from users.models import User
from .serializers import UserSerializer
from rest_framework.permissions import BasePermission

class IsAuthenticatedOrReadOnly(BasePermission):
  AuthMethods = ['PUT', 'PATCH']
  def has_permission(self, request, view):
    if(request.method in self.AuthMethods):
      if((not request.user) or
        (not request.user.is_authenticated) or
        (request.user.id != view.kwargs['pk'])):
        return False

    return True

class UserDetailView(generics.RetrieveUpdateAPIView):
  serializer_class = UserSerializer
  queryset = User.objects.all()
  permission_classes = [IsAuthenticatedOrReadOnly]
  
  
