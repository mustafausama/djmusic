from django import forms

class CreateArtistForm(forms.Form):
  stage_name = forms.CharField(label='Stage Name', max_length=200)
  social_link = forms.CharField(label="Social Link", required=False)
