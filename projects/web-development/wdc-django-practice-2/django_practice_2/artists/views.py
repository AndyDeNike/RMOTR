from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import Artist
# from .models import Artist, Song


def artists(request):
    """
        PART 1:
            - Task 1: Implement a view under /artists URL that fetches all
            Artist's objects stored in the DB and render the 'artists.html'
            template sending all 'artists' as context.

            - Task 2: In the same view, check if a 'first_name' GET parameter
            is sent. If so, filter the previous queryset with ALL artists, in
            order to filter only the ones that contains the given pattern in its
            first_name

            - Task 3: Similar to previous task, take the 'popularity' GET
            parameter (if its given) and filter all the artists that have a
            popularity greater or equal to the one given.

        PART 2:
            - Task 2: After adding a new 'genre' CharField to the Artist model
            in models.py with some choices, add to this view a new filter
            from a 'genre' GET param (if given), in a similar way to the tasks
            before. If genre param is given, filter the artists queryset only with
            artists from that genre.
    """
    artists = Artist.objects.all()
    
    #pass first_name parameter in url as so: 
    #http://wdc-django-practice-2.c9users.io:8080/artists/?first_name=Ed
    first_name = request.GET.get('first_name')
    if first_name:
        artists = artists.filter(first_name__icontains=first_name)
    
    popularity = request.GET.get('popularity')
    if popularity: 
        artists = artists.filter(popularity__gte=popularity)
        
    genre = request.GET.get('genre')
    if genre:
        artists = artists.filter(genre=genre)

    return render(request, 'artists.html', context={'artists': artists})

def artist(request, artist_id):
    """
        PART 1:
            - Task 4: Implement a view under /artists/<artist_id> that takes the
            given artist_id in the URL and gets the proper Artist object from
            the DB. Then render the 'artist.html' template sending the 'artist'
            object as context
    """
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        return HttpResponseNotFound()
    
    return render(request, 'artist.html', context={'artist': artist})


def songs(request, artist_id=None):
    """
        PART 3:
            - Task 2: After creating the new Song model with its migration,
            implement a view under /songs URL that display ALL the songs stored
            in the DB. In order to do this, fetch all the Song objects and
            render the 'songs.html' sending the 'songs' queryset as context.
            Before rendering the template, loop through the songs queryset and
            for each song, fetch the proper Artist object that matches with the
            artist_id from the song. Once you have the song's artist object, add
            it like 'song.artist = artist'.

            - Task 3: Add a 'title' filter from a 'title' GET parameter (if given)
            that filters the 'songs' queryset for songs that contains that
            pattern, in a similar way that the tasks before.

            - Task 4: Add a new /songs/<artist_id> URL that points to this
            same view. If the artist_id is given, filter the songs queryset for
            songs that match with given artist_id and render the same 'songs.html'
            template.
    """
    pass
