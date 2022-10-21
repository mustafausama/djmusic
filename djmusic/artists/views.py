from django.shortcuts import redirect, render

from .forms import CreateArtistForm
from .models import Artist
from django.views import generic
from django.db.models import F

def create_artist(request):
  error = None
  if request.method == 'POST':
    form = CreateArtistForm(request.POST)
    
    if form.is_valid():

      if Artist.objects.filter(stage_name=form.cleaned_data['stage_name']).exists():
        form.add_error('stage_name', 'Stage name already exists')
        error = 'Data Error: Please follow the instructions'
      else:
        new_artits = Artist(stage_name=form.cleaned_data['stage_name'], social_link=form.cleaned_data['social_link'])
        new_artits.save()
      
        return redirect('artists:list')
    else:
      error = 'Filling Error: Please fill all the required fields correctly'
  
  else:
    form = CreateArtistForm()
  
  return render(request, 'artists/create.html', {'form': form, 'error': error})

class ArtistList(generic.ListView):
  context_object_name = 'artists_albums'
  template_name = 'artists/list.html'
  
  # Get all albums grouped and ordered by artists in one SQL query
  def get_queryset(self):
    # Selection with join then annotate and select values
    return \
      Artist.objects.all().prefetch_related('album_set').order_by('id') \
      .values('id', 'stage_name', 'social_link', 'album__id', 'album__album_name', 'album__created', 'album__released_at', 'album__cost')
  
    # return Album.objects.order_by('artist').annotate(stage=F('artist__stage_name'), social=F('artist__social_link'), album=F('album_name')).values('stage', 'artist_id', 'social', 'id', 'album', 'created', 'released_at', 'cost')
  
  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    data_list = list(context['artists_albums'])
    organized_data = {}
    for entry in data_list:
      if entry['stage_name'] not in organized_data:
        organized_data[entry['stage_name']] = {'id': entry['id'], 'social_link': entry['social_link'], 'albums': []}
      organized_data[entry['stage_name']]['albums'].append(entry)
    
    context['artists_albums'] = organized_data
    print(context['artists_albums'])
    return context
    