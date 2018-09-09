from django import forms

from .models import GENRE_CHOICES, Song

class ArtistForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    picture_url = forms.URLField(label='Picture url')
    popularity = forms.IntegerField(label='Popularity')
    genre = forms.CharField(label='Genre', max_length=100)


class SongForm(forms.Form):
    pass
