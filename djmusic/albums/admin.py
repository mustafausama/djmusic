from django import forms
from django.contrib import messages
from django.contrib import admin
from django.utils.translation import ngettext
from albums.models import Album
from django.utils.translation import gettext_lazy as _

class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    exclude = []
    help_texts = {
      'is_approved': _('Approve the album if its name is not explicit')
    }

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
  form = AlbumForm

  list_display = ('album_name', 'is_approved')
  fields = (('album_name', 'artist'), ('released_at', 'created'), 'cost', 'is_approved', 'modified')
  readonly_fields = ('created', 'modified')

  actions = ['make_approved']
  actions_selection_counter = True


  @admin.action(description='Mark selected albums as approved')
  def make_approved(self, request, queryset):
    updated = queryset.update(is_approved=True)
    self.message_user(request, ngettext(
      "%d album was successfully approved",
      "%d albums were successfully approved", updated) % updated, messages.SUCCESS)
