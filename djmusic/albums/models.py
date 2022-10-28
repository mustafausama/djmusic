from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.html import mark_safe

from .validators import validate_audio_file_extension

class Album(TimeStampedModel):
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  album_name = models.CharField(max_length=200, default='New Album')
  released_at = models.DateTimeField(blank=False)
  cost = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
  is_approved = models.BooleanField(default=False)
  # From TimeStampedModel, we have:
  ## created
  ## modified
  
  def __str__(self):
    return self.album_name


class SongDeleteQuerySet(models.QuerySet):
  def delete(self, *args, **kwargs):
    error = []
    for obj in self:
      if(obj.album.song_set.count() == 1):
        error.append(str('Cannot delete the song ' + obj.name + ' because it is the only one belonging to the album ' + obj.album.album_name))
    if len(error) > 0:
      print(error)
      raise Exception(error)
    super(SongDeleteQuerySet, self).delete(*args, **kwargs)

class Song(TimeStampedModel):
  objects = SongDeleteQuerySet.as_manager()
  
  album = models.ForeignKey(Album, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=True, blank=True)
  image = models.ImageField(upload_to='song_images', null=False)
  image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(100, 50)], format='JPEG', options={'quality': 60})
  audio = models.FileField(upload_to='song_audio', validators=[validate_audio_file_extension])
  
  
  def delete(self, *args, **kwargs):
    if(self.album.song_set.count() == 1):
      raise Exception('Cannot delete the song ' + self.name + ' because it is the only one belonging to the album ' + self.album.album_name)
    super(Song, self).delete(*args, **kwargs)
  
  # Default value of song is the album name
  def save(self, *args, **kwargs):
    if self.name is None:
      self.name = self.album.album_name
    super(Song, self).save(*args, **kwargs)
    

  def image_tag(self):
    if self.image:
        return mark_safe('<img src="%s" width="20" />' % self.image.url)
    else:
        return '(No Image)'
  image_tag.short_description = 'Thumbnail'
  
  def audio_tag(self):
    if self.audio:
        return mark_safe('<audio controls><source src="%s"></audio>' % self.audio.url)
    else:
        return '(No Image)'
  audio_tag.short_description = 'Audio'
