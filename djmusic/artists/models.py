from django.db import models
from django.db.models import F

class Artist(models.Model):
  stage_name = models.CharField(max_length=200, unique=True, blank=False)
  # TextField has null=False by default
  social_link = models.TextField(blank=True)
  
  def __str__(self):
    return self.stage_name
  
  class Meta:
    ordering = ['stage_name']
