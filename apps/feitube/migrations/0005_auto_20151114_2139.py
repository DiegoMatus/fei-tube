# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feitube', '0004_video_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='favs',
            field=models.ManyToManyField(related_name='videos_fav', verbose_name='Favoritos', null=True, to='feitube.Profile', blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='favs_count',
            field=models.IntegerField(verbose_name='Cantidad de favoritos', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='profile',
            field=models.ForeignKey(verbose_name='Usuario', null=True, to='feitube.Profile', blank=True, related_name='videos'),
        ),
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.IntegerField(verbose_name='Visitas', null=True, blank=True),
        ),
    ]
