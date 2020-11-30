from django.shortcuts import render, redirect, get_object_or_404
from . models import Movie, Genre
from . forms import GenreForm, MovieForm



def index(request):
    num_movies=Movie.objects.all()
    
    return render(
        request,
        'index.html',
        context={'num_movies':num_movies},
    )
# Create your views here. 

def movies(request):
    num_movies=Movie.objects.all()
    
    return render(
        request,
        'movies.html',
        context={'num_movies':num_movies},
    )

def contacto(request):
    
    return render(
        request,
        'contacto.html',
    )




    
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic


class GenreDelete(DeleteView):
    model = Genre
    success_url = reverse_lazy('index')


class GenreDetailView(generic.DetailView):
    model = Genre
    
class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('index')
    
class MovieDetailView(generic.DetailView):
    model = Movie

class GenreListView(generic.ListView):
    model = Genre
    template_name = 'templates/peliculas/genre_list.html'
    queryset = Genre.objects.all()

    paginate_by = 10


def genre_new(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('genre-detail', pk=post.pk)
    else:
        form = GenreForm()
        return render(request, 'peliculas/genre_form.html', {'form': form})

def genre_edit(request, pk):
    post = get_object_or_404(Genre, pk=pk)
    if request.method == "POST":
        form = GenreForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('genre-detail', pk=post.pk)
    else:
        form = GenreForm(instance=post)
    return render(request, 'peliculas/genre_form.html', {'form': form})

def movie_new(request):
    if request.method == "POST":
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #form.save_m2m()
            return redirect('movie-detail', pk=post.pk)
    else:
        form = MovieForm()
        return render(request, 'peliculas/movie_form.html', {'form': form})

def movie_edit(request, pk):
    post = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('movie-detail', pk=post.pk)
    else:
        form = MovieForm(instance=post)
    return render(request, 'peliculas/movie_form.html', {'form': form})
