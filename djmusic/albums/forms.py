from django import forms

from .models import Album

class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'

class CreateAlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = ['artist', 'album_name', 'released_at', 'cost']
    widgets = {
      'released_at': forms.DateTimeInput(attrs={'type': 'datetime-local'})
    }
  
