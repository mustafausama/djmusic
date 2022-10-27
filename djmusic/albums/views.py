from django.shortcuts import redirect, render
from django.views import View

from .models import Album
from .forms import CreateAlbumForm

class create_album(View):
  def get(self, request):
    form = CreateAlbumForm()
    return render(request, 'albums/create.html', {'form': form})
  
  def post(self, request):
    error = None
    form = CreateAlbumForm(request.POST)
    
    if form.is_valid():
      new_album = Album(artist=form.cleaned_data['artist'], album_name=form.cleaned_data['album_name'], released_at=form.cleaned_data['released_at'], cost=form.cleaned_data['cost'])
      new_album.save()
      return redirect('artists:list')
    else:
      error = 'Filling Error: Please fill all the required fields correctly'
    return render(request, 'albums/create.html', {'form': form, 'error': error})
