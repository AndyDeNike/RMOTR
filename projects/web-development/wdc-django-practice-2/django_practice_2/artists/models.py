from django.db import models


GENRE_CHOICES = (
    ("rock", "Rock"),
    ("pop", "Pop"),
)

class Artist(models.Model):
    """
        PART 2:
            - Task 1: Add a new 'genre' field to this model. The field's type
            must be CharField and in this case it will have 'choices' option
            with the GENRE_CHOICES given above.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    artistic_name = models.CharField(max_length=255)
    picture_url = models.URLField()
    popularity = models.IntegerField()
    genre = models.CharField(choices=GENRE_CHOICES, max_length=255)


# class Song(models.Model):
#     """
#         PART 3:
#             - Task 1: Implement the Song model with the following fields:
#                 * artist_id (type: integer)
#                 * title (type: char)
#                 * album_name (type: char)
#     """
#     pass
