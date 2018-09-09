from django import forms

from .models import GENRE_CHOICES, Artist #this was defaulted as Song (wrong)

class ArtistForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100, required=False)
    last_name = forms.CharField(label='Last name', max_length=100, required=False)
    picture_url = forms.URLField(label='Picture url', required=False)
    popularity = forms.IntegerField(label='Popularity', required=False)
    genre = forms.ChoiceField(label='Genre', choices=GENRE_CHOICES, required=False)

class SongForm(forms.Form):
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    title = forms.CharField(max_length=100)
    album_name = forms.CharField(max_length=100)
