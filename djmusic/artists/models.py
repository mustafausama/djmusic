from django.db import models
from django.db.models import Count, Q

class ArtistManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().annotate(approved_albums=Count('album__is_approved', filter=Q(album__is_approved=True)))

class Artist(models.Model):
  objects = ArtistManager()
  stage_name = models.CharField(max_length=200, unique=True, blank=False)
  # TextField has null=False by default
  social_link = models.TextField(blank=True)

  def __str__(self):
    return self.stage_name
  
  class Meta:
    ordering = ['stage_name']
