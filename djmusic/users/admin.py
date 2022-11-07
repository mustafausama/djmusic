from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django import forms

class UserModelForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = User
        fields = '__all__'
        exclude = ('password', )

class UserAdmin(admin.ModelAdmin):
  form = UserModelForm

admin.site.register(User, UserAdmin)
