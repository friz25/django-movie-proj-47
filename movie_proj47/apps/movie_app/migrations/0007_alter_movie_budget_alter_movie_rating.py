# Generated by Django 4.0.4 on 2022-06-04 10:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_alter_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(blank=True, default=1000000, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
