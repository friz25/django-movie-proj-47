# Generated by Django 4.0.4 on 2022-06-04 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('EUR', 'Euro'), ('USD', 'Dollars'), ('RUB', 'Rubles')], default='RUB', max_length=3),
        ),
    ]
