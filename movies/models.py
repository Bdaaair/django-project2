from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Genre(models.Model):
    name = models.CharField(max_length=30)
    
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=150)
    actors = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,related_name="movies")
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="movie_users")

class Watchlist(models.Model):
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name="watchlists")

class Review(models.Model):
    review = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_reviews")

