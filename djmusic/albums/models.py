from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel

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