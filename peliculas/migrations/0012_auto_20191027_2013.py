# Generated by Django 2.2.6 on 2019-10-27 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0011_auto_20191027_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.CharField(default='', max_length=100),
        ),
    ]
