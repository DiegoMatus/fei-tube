# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feitube', '0007_auto_20151114_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='rates',
            field=models.ManyToManyField(through='feitube.Rate', related_name='videos_rate', to='feitube.Profile', blank=True, verbose_name='Calificaciones'),
        ),
    ]
