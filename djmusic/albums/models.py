from django.db import models
from artists.models import Artist

class Album(models.Model):
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  album_name = models.CharField(max_length=200, default='New Album')
  created_at = models.DateTimeField(auto_now_add=True)
  released_at = models.DateTimeField(blank=False, auto_now_add=True)
  cost = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
  
  def __str__(self):
    return self.album_name