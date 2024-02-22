from django.core.validators import MinValueValidator
from django.db import models

from exam_prep_my_music_app.profiles.models import Profile

'''
o	Owner
    	A foreign key to the Profile model.
       Establishes a many-to-one relationship with the Profile model, associating each album with a profile.
    	The ON DELETE constraint must be configured to an appropriate value in alignment with the specified additional tasks.
    	This field should remain hidden in forms.
'''
'''
o	Genre
    	Character field, required.
    	It should consist of a maximum of 30 characters.
    	The choices are "Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music", "Hip Hop Music", and "Other".
'''


class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MAX_GENRE_LENGTH = 30
    MIN_PRICE = 0.0

    GENRE_POP_MUSIC = "Pop Music"
    GENRE_JAZZ_MUSIC = "Jazz Music"
    GENRE_R_B_MUSIC = "R&B Music"
    GENRE_ROCK_MUSIC = "Rock Music"
    GENRE_COUNTRY_MUSIC = "Country Music"
    GENRE_DANCE_MUSIC = "Dance Music"
    GENRE_HIP_HOP_MUSIC = "Hip Hop Music"
    GENRE_OTHER = "Other"

    GENRES = (
        (GENRE_POP_MUSIC, GENRE_POP_MUSIC),
        (GENRE_JAZZ_MUSIC, GENRE_JAZZ_MUSIC),
        (GENRE_R_B_MUSIC, GENRE_R_B_MUSIC),
        (GENRE_ROCK_MUSIC, GENRE_ROCK_MUSIC),
        (GENRE_COUNTRY_MUSIC, GENRE_COUNTRY_MUSIC),
        (GENRE_DANCE_MUSIC, GENRE_DANCE_MUSIC),
        (GENRE_HIP_HOP_MUSIC, GENRE_HIP_HOP_MUSIC),
        (GENRE_OTHER, GENRE_OTHER),
    )

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Album Name",
    )

    artist_name = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        null=False,
        blank=False,
        verbose_name="Artist",
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=GENRES,
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(MinValueValidator(MIN_PRICE),
                    )
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL",
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
    )
