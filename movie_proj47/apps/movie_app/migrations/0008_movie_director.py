# Generated by Django 4.0.4 on 2022-06-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0007_alter_movie_budget_alter_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='Квентин Тарантино', max_length=100),
        ),
    ]
