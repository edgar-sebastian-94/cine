# Generated by Django 2.2.6 on 2019-10-27 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0008_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.URLField(default='', max_length=100),
        ),
    ]
