"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import UserCreateAPIView, UserLoginAPIView
from movies.views import CreateMovieListView, Createwatchlistview, CreateReviewview, CreatGenreListview


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', UserCreateAPIView.as_view(),name="api_register"),   
    path('api/login/',UserLoginAPIView.as_view(),name="api_login"),
    path('api/movie/create/', CreateMovieListView.as_view(),name="api_createmovie"), 
    path('api/watchlist/create/', Createwatchlistview.as_view(),name="api_watchlist" ),
    path('api/review/create/', CreateReviewview.as_view(), name="api_review" ),
    path('api/genre/create/', CreatGenreListview.as_view(), name= "api_genre"),
]
