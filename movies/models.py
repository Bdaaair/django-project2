from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Movies_Model(models.Model):
    name = models.CharField(max_length=150)
    actors = models.CharField(max_length=100)
    release_date = models.DateField()
    
class Watchlist_Model(models.Model):
    name = models.CharField(max_length=30)

class Genre_Model(models.Model):
    name = models.CharField(max_length=30)

class Rating_Reviews(models.Model):
    reviws_field = models.TextField()
    


