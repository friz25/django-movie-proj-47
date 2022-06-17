from django.urls import path

from . import views

app_name="movie_app"
urlpatterns = [
    path('', views.show_all_movies, name = 'show_all_movies'),
    path('movie/<int:id_movie>', views.show_one_movie, name = 'movie-detail'),
    path('directors/<int:id_director>', views.show_one_director, name = 'director-detail'),
    path('actors/<int:id_actor>', views.show_one_actor, name = 'actor-detail'),
]
