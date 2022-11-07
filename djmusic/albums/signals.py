from django.db.models.signals import pre_delete
from .models import Song
from django.dispatch import receiver
from django.db.models import QuerySet

@receiver(pre_delete, sender=Song, weak=True, dispatch_uid='delete')
def validate_deletion(sender, instance, **kwargs):
  
  if(type(kwargs['origin']) is not QuerySet):
    if(instance.album.song_set.count() == 1):
      raise Exception('Cannot delete the song ' + instance.name + ' because it is the only one belonging to the album ' + instance.album.album_name)
  else:
    rem = {}
    for q in kwargs['origin']:
      if(q.album.id not in rem):
        rem[q.album.id] = q.album.song_set.count()
      rem[q.album.id] -= 1
      if(rem[q.album.id] == 0):
        raise Exception('Cannot delete the selected songs because that would leave albums with no songs')

  