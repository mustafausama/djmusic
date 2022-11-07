from django import forms
from django.contrib import messages
from django.contrib import admin
from django.utils.translation import ngettext
from albums.models import Album, Song
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

class SongInlineFormset(forms.models.BaseInlineFormSet):

  def clean(self):
    count = 0
    delete_count = 0
    for form in self.forms:
      try:
        if form.cleaned_data:
          count += 1
          if form.cleaned_data['DELETE']:
            delete_count = delete_count + 1
      except AttributeError:
        pass
    
    if delete_count == count:
      raise forms.ValidationError("You must have at least one song")

class SongInline(admin.TabularInline):
  formset = SongInlineFormset
  model = Song


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
  inlines = [SongInline]

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


class SongForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['image'].required = True

  class Meta:
    model = Song
    exclude = []
    help_texts = {
      'name': _('If left blank, name will default to album name'),
      'image_tag': _('Current image thumbnail'),
      'audio_tag': _('Current playable audio')
    }

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
  form = SongForm
  list_display = ('name', 'image_tag', 'album')
  fields = ('album', 'name', ('image', 'image_tag'), ('audio', 'audio_tag'))
  readonly_fields = ('image_tag', 'audio_tag')

  def delete_model(self, request, obj) -> None:
    try:
      super().delete_model(request, obj)
    except Exception as e:
      messages.set_level(request, messages.ERROR)
      self.message_user(request, e, level=messages.ERROR)

  def delete_queryset(self, request, queryset) -> None:
    try:
      super().delete_queryset(request, queryset)
    except Exception as e:
      messages.set_level(request, messages.ERROR)
      self.message_user(request, e, level=messages.ERROR)
