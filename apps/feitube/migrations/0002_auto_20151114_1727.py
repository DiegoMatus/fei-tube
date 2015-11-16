# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feitube', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rate',
            options={'verbose_name_plural': 'Calificaciones', 'verbose_name': 'Calificación'},
        ),
        migrations.AlterField(
            model_name='rate',
            name='score',
            field=models.IntegerField(verbose_name='Puntuación'),
        ),
        migrations.AlterField(
            model_name='video',
            name='favs',
            field=models.ManyToManyField(related_name='videos_fav', to='feitube.Profile', verbose_name='Favoritos'),
        ),
        migrations.AlterField(
            model_name='video',
            name='favs_count',
            field=models.IntegerField(verbose_name='Cantidad de favoritos'),
        ),
        migrations.AlterField(
            model_name='video',
            name='rates',
            field=models.ManyToManyField(through='feitube.Rate', related_name='videos_rate', to='feitube.Profile', verbose_name='Calificaciones'),
        ),
    ]
