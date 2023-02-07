from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Movie, Watchlist, Review
from .serializers import CreateMovieList


class CreateView(CreateAPIView):
    serializer_class = CreateMovieList

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)