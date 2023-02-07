from rest_framework import serializers
from .models import Movie

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'actors', 'genre','release_date','rating','reviews']
