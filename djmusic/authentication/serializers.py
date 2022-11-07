from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
  username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
  email = serializers.EmailField(required=False)
  password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

  # Case insensitive validation
  def validate_email(self,value):
    if User.objects.filter(email=value.lower()).exists():
      raise serializers.ValidationError("This field must be unique.")
    return value.lower()

  def validate(self, attrs):
    if(attrs['password1'] != attrs['password2']):
      raise serializers.ValidationError({"password2": "Password fields do not match"})
    
    return attrs
  
  def create(self, validated_data):
    if('email' not in validated_data):
      validated_data['email'] = ''

    user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'].lower(), password=validated_data['password1'])    
    
    return user
  