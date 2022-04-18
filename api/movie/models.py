from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Genres(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    language = models.CharField(max_length=25)
    overview = models.TextField()
    poster = models.ImageField(
        upload_to="movie/poster", null=True, blank=True)
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1990),
                    MaxValueValidator(datetime.now().year)],
        help_text="Use only year")
    genres = models.ManyToManyField(
        Genres, blank=True, related_name="movies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
