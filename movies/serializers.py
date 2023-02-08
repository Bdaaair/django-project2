from rest_framework import serializers
from .models import Movie, Watchlist, Review, Genre


class CreateMovieListserializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Movie
        fields = ['id','user','name', 'actors', 'release_date', 'genre']

class CreatWatchListserializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ['movies']

class CreatReviewListserializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['review', 'movie', 'user']


class CreatGenreListserializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']