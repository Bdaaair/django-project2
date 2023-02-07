from rest_framework import serializers
from rest_framework import serializers
from .models import Movies_Model

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies_Model
        fields = ['id', 'actors', 'genre','release_date','rating','reviews']
