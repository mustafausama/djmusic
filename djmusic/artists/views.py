from django.urls import reverse_lazy
from .forms import CreateArtistForm
from .models import Artist
from django.views.generic import ListView
from django.views.generic.edit import FormView

class create_artist(FormView):
  
  form_class = CreateArtistForm
  template_name = 'artists/create.html'
  success_url = reverse_lazy('artists:list')

  def form_valid(self, form):
      if Artist.objects.filter(stage_name=form.cleaned_data['stage_name']).exists():
        form.add_error('stage_name', 'Stage name already exists')
        error = 'Data Error: Please follow the instructions'
        return super().render_to_response({'error': error, 'form': form})
      else:
        new_artits = Artist(stage_name=form.cleaned_data['stage_name'], social_link=form.cleaned_data['social_link'])
        new_artits.save()
        return super().form_valid(form);

  def form_invalid(self, form):
    error = 'Filling Error: Please fill all the required fields correctly'
    return super().render_to_response({'error': error, 'form': form})


class ArtistList(ListView):
  context_object_name = 'artists_albums'
  template_name = 'artists/list.html'
  
  # Get all albums grouped and ordered by artists in one SQL query
  def get_queryset(self):
    # Selection with join
    return \
      Artist.objects.all().prefetch_related('album_set').order_by('id') \
      .values('id', 'stage_name', 'social_link', 'album__id', 'album__album_name', 'album__created', 'album__released_at', 'album__cost')
    
  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    data_list = list(context['artists_albums'])
    organized_data = {}
    for entry in data_list:
      if entry['stage_name'] not in organized_data:
        organized_data[entry['stage_name']] = {'id': entry['id'], 'social_link': entry['social_link'], 'albums': []}
      organized_data[entry['stage_name']]['albums'].append(entry)
    
    context['artists_albums'] = organized_data
    return context
    