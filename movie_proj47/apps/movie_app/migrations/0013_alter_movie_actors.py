# Generated by Django 4.0.4 on 2022-06-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0012_alter_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='movie_app.actor'),
        ),
    ]
