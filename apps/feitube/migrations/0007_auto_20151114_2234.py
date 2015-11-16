# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feitube', '0006_auto_20151114_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='favs',
            field=models.ManyToManyField(to='feitube.Profile', related_name='videos_fav', verbose_name='Favoritos'),
        ),
        migrations.AlterField(
            model_name='video',
            name='profile',
            field=models.ForeignKey(related_name='videos', verbose_name='Usuario', to='feitube.Profile'),
        ),
    ]
