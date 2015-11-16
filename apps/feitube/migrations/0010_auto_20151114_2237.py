# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feitube', '0009_auto_20151114_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='favs',
            field=models.ManyToManyField(blank=True, related_name='videos_fav', verbose_name='Favoritos', to='feitube.Profile'),
        ),
        migrations.AlterField(
            model_name='video',
            name='rates',
            field=models.ManyToManyField(related_name='videos_rate', verbose_name='Calificaciones', through='feitube.Rate', to='feitube.Profile'),
        ),
    ]
