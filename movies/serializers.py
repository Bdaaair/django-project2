from rest_framework import serializers
from .models import Movie, Watchlist, Review


class CreateMovieListserializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','name', 'actors', 'release_date', 'genre']

class CreatWatchListserializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ['movies']

class CreatReviewListserializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['review', 'movie', 'user']