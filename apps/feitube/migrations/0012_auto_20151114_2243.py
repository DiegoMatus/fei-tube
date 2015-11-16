# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feitube', '0011_auto_20151114_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='profile',
            field=models.ForeignKey(blank=True, related_name='videos', verbose_name='Usuario', null=True, to='feitube.Profile'),
        ),
    ]
