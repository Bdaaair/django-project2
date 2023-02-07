from rest_framework import serializers
from .models import Movie


class CreateMovieList(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','name', 'actors', 'release_date', 'genre']
        