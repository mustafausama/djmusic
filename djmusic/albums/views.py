from django.shortcuts import redirect, render

from .models import Album
from .forms import CreateAlbumForm

def create_album(request):
  error = None
  if request.method == 'POST':
    form = CreateAlbumForm(request.POST)
    
    if form.is_valid():
      new_album = Album(artist=form.cleaned_data['artist'], album_name=form.cleaned_data['album_name'], released_at=form.cleaned_data['released_at'], cost=form.cleaned_data['cost'])
      new_album.save()
      return redirect('artists:list')
    else:
      error = 'Filling Error: Please fill all the required fields correctly'
  
  else:
    form = CreateAlbumForm()
  
  return render(request, 'albums/create.html', {'form': form, 'error': error})
