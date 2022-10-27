from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .models import Album
from .forms import CreateAlbumForm

class create_album_form(FormView):
  
  form_class = CreateAlbumForm
  template_name = 'albums/create.html'
  success_url = reverse_lazy('artists:list')
  
  def form_valid(self, form):
      new_album = Album(artist=form.cleaned_data['artist'], album_name=form.cleaned_data['album_name'], released_at=form.cleaned_data['released_at'], cost=form.cleaned_data['cost'])
      new_album.save()
      return super().form_valid(form)

  def form_invalid(self, form):
    error = 'Filling Error: Please fill all the required fields correctly'
    return super().render_to_response({'error': error, 'form': form})

