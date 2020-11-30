from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('movies/', views.movies, name='movies'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('contacto/', views.contacto, name='contacto'),
    path('genre/<int:pk>', views.GenreDetailView.as_view(), name='genre-detail'),
    path('movie/<str:pk>', views.MovieDetailView.as_view(), name='movie-detail'),
]

urlpatterns += [
    path('genre/create/', views.genre_new,name='genre_create'),
    path('genre/<int:pk>/update/', views.genre_edit, name='genre_update'),
    path('genre/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre_delete'),
    path('movie/create/', views.movie_new,name='movie_create'),
    path('movie/<str:pk>/update/', views.movie_edit, name='movie_update'),
    path('movie/<str:pk>/delete/', views.MovieDelete.as_view(), name='movie_delete'),
]