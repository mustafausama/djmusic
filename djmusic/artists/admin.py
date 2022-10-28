from django.contrib import admin
from artists.models import Artist


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
  
  list_display = ('stage_name', 'albums', 'approved_albums')
  
  readonly_fields = ('approved_albums', 'albums')
  
  fieldsets = (
    (None, {
      'fields': ('stage_name', 'social_link')
    }),
    (None, {
      'fields': ('albums',),
      'description': 'Number of albums beloning to this artist'
    }),
    (None, {
      'fields': ('approved_albums',),
      'description': 'Number of approved albums for this artist'
    })
  )
  
  def albums(self, obj):
    return obj.album_set.count()
  
  def approved_albums(self, obj):
    return obj.approved_albums
