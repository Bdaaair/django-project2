from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Movies_Model,Watchlist_Model,Genre_Model,Rating_Reviews


# Create your views here.


class MoviesView(ListAPIView):
    queryset = Movies_Model.objects.all()