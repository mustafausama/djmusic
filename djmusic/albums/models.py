from django.db import models
from django.utils import timezone
from artists.models import Artist

class Album(models.Model):
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  album_name = models.CharField(max_length=200, default='New Album')
  created_at = models.DateTimeField(default=timezone.now)
  released_at = models.DateTimeField(blank=False)
  cost = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
  is_approved = models.BooleanField(default=False)
  
  def __str__(self):
    return self.album_name