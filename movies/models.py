from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=30)
    duration = models.DurationField()
    genre = models.ManyToManyField(Genre, blank=True)
    language = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField()
    poster = models.ImageField(upload_to="movie_posters", null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title
