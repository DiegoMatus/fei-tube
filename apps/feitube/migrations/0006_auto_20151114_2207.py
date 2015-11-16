# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.feitube.models


class Migration(migrations.Migration):

    dependencies = [
        ('feitube', '0005_auto_20151114_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='path',
            field=models.FileField(upload_to=apps.feitube.models.get_file_path_videos, null=True, blank=True),
        ),
    ]
