from django.test import TestCase
from peliculas.models import Genre, Movie

class GenreModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Genre.objects.create(name='Accion', summary='Prueba')
    
    def test_name_label(self):
        genre=Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_summary_label(self):
        genre=Genre.objects.get(id=1)
        field_label = genre._meta.get_field('summary').verbose_name
        self.assertEquals(field_label,'summary')
    
    def test_name_max_length(self):
        genre=Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length,100)
    
    def test_summary_max_length(self):
        genre=Genre.objects.get(id=1)
        max_length = genre._meta.get_field('summary').max_length
        self.assertEquals(max_length,1000)
        
    def test_get_absolute_url(self):
        genre=Genre.objects.get(id=1)
        self.assertEquals(genre.get_absolute_url(), '/peliculas/genre/1')

class MovieModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        g = Genre.objects.create(name='Accion', summary='Prueba')
        test_movie = Movie.objects.create(id= '44fc2b9d-2b04-45cb-af8a-c4601527b156', title='Rey Leon',summary='Prueba', genre=g, url='https://www.youtube.com/embed/rslZ-fHiSuI')
    
    def test_title_label(self):
        movie= Movie.objects.get(id= '44fc2b9d-2b04-45cb-af8a-c4601527b156')
        field_label = movie._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_summary_label(self):
        movie=Movie.objects.get(id='44fc2b9d-2b04-45cb-af8a-c4601527b156')
        field_label = movie._meta.get_field('summary').verbose_name
        self.assertEquals(field_label,'summary')
    
    def test_genre_label(self):
        movie=Movie.objects.get(id='44fc2b9d-2b04-45cb-af8a-c4601527b156')
        field_label = movie._meta.get_field('genre').verbose_name
        self.assertEquals(field_label,'genre')
    
    def test_title_max_length(self):
        movie=Movie.objects.get(id='44fc2b9d-2b04-45cb-af8a-c4601527b156')
        max_length = movie._meta.get_field('title').max_length
        self.assertEquals(max_length,200)
    
    def test_summary_max_length(self):
        movie=Movie.objects.get(id='44fc2b9d-2b04-45cb-af8a-c4601527b156')
        max_length = movie._meta.get_field('summary').max_length
        self.assertEquals(max_length,1000)
        
    def test_get_absolute_url(self):
        movie=Movie.objects.get(id='44fc2b9d-2b04-45cb-af8a-c4601527b156')
        self.assertEquals(movie.get_absolute_url(), '/peliculas/movie/44fc2b9d-2b04-45cb-af8a-c4601527b156')
