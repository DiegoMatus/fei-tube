# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feitube', '0002_auto_20151114_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='favs_count',
            field=models.IntegerField(verbose_name='Cantidad de favoritos', null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.IntegerField(verbose_name='Visitas', null=True),
        ),
    ]
