from django.test import TestCase
from peliculas.forms import GenreForm, MovieForm
from peliculas.models import Genre, Movie
from django.core.files.uploadedfile import SimpleUploadedFile

class GenreFormsTest(TestCase):
    def test_valid_form(self):
        g = Genre.objects.create(name='Prueba1', summary='Prueba')
        data = {'name': g.name, 'summary': g.summary,}
        form = GenreForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = Genre.objects.create(name='', summary='Prueba')
        data = {'name': g.name, 'summary': g.summary,}
        form = GenreForm(data=data)
        self.assertFalse(form.is_valid())

class MovieFormsTest(TestCase):
    def test_valid_form(self):
        genre = Genre.objects.create(name='1', summary='Prueba')
        genre = Genre.objects.get(pk=1).pk
        m = Movie.objects.create(title='Prueba1', summary='Prueba', url='https://www.youtube.com/embed/rslZ-fHiSuI')
        m.save()
        data = {'title': m.title, 'summary': m.summary, 'genre': genre, 'url' : m.url, }
        
        with open('peliculas/static/img/logo.png', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/png')
        
        form = MovieForm(data, {'image': document})
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = Genre.objects.create(name='Accion', summary='Prueba')
        m = Movie.objects.create(title='', summary='Prueba', genre=g, url='https://www.youtube.com/embed/rslZ-fHiSuI')
        data = {'title': m.title, 'summary': m.summary, 'genre': m.genre, 'url' : m.url, }
        form = MovieForm(data=data)
        self.assertFalse(form.is_valid())