from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Movie, Watchlist, Review
from .serializers import CreateMovieListserializer, CreatWatchListserializer, CreatReviewListserializer,CreatGenreListserializer 


class CreateMovieListView(CreateAPIView):
    serializer_class = CreateMovieListserializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class Createwatchlistview(CreateAPIView):
    serializer_class = CreatWatchListserializer

class CreateReviewview(CreateAPIView):
    serializer_class = CreatReviewListserializer

class CreatGenreListview(CreateAPIView):
    serializer_class = CreatReviewListserializer