# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feitube', '0008_auto_20151114_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='rates',
            field=models.ManyToManyField(null=True, to='feitube.Profile', verbose_name='Calificaciones', blank=True, through='feitube.Rate', related_name='videos_rate'),
        ),
    ]
