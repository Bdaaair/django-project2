from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Movie, Watchlist, Review
from .serializers import CreateMovieListserializer, CreatWatchListserializer, CreatReviewListserializer,CreatGenreListserializer 
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class CreateMovieListView(CreateAPIView):
    serializer_class = CreateMovieListserializer
    permission_classes = [IsAdminUser]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class Createwatchlistview(CreateAPIView):
    serializer_class = CreatWatchListserializer

class CreateReviewview(CreateAPIView):
    serializer_class = CreatReviewListserializer

class CreatGenreListview(CreateAPIView):
    serializer_class = CreatGenreListserializer
    permission_classes = [IsAdminUser]