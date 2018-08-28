from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from artists.models import Artist
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Imports initial data version 1'

    def handle(self, *args, **options):
        User.objects.all().delete()
        Artist.objects.all().delete()

        User.objects.create_superuser(
            username='admin', email='admin@example.com', password='admin')

        ARTISTS = [
            ('Stevland', 'Judkins', 'Stevie Wonders', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Stevie_Wonder_1973.JPG/600px-Stevie_Wonder_1973.JPG', 90, 'rock'),
            ('James', 'Hendrix', 'Jimi Hendrix', 'https://upload.wikimedia.org/wikipedia/commons/a/ae/Jimi_Hendrix_1967.png', 80, 'rock'),
            ('Edward', 'Sheeran', 'Ed Sheeran', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Ed_Sheeran_2013.jpg/500px-Ed_Sheeran_2013.jpg', 75, 'pop'),
        ]
        for first_name, last_name, artistic_name, picture_url, popularity, genre in ARTISTS:
            Artist.objects.create(
                first_name=first_name,
                last_name=last_name,
                artistic_name=artistic_name,
                picture_url=picture_url,
                popularity=popularity,
                genre=genre
            )
        print('Imported!')
