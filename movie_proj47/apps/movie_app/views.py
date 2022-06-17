from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import F, Sum, Avg, Max, Min, Count

from .models import Movie, Director, Actor

def show_all_movies(request):
    movies = Movie.objects.order_by(F('year').desc(nulls_first=True), '-rating')
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))
    return render(request, 'movie_app/all_movies.html', {
        'movies':movies,
        'agg':agg,
        'total':movies.count()
    })
def show_one_movie(request, id_movie:int):
    movie = get_object_or_404(Movie, id=id_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie':movie
    })
def show_one_director(request, id_director:int):
    director = get_object_or_404(Director, id=id_director)
    return render(request, 'movie_app/one_director.html', {
        'director':director
    })
def show_one_actor(request, id_actor:int):
    actor = get_object_or_404(Actor, id=id_actor)
    return render(request, 'movie_app/one_actor.html', {
        'actor':actor
    })
