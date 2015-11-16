# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.feitube.models


class Migration(migrations.Migration):

    dependencies = [
        ('feitube', '0003_auto_20151114_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='path',
            field=models.FileField(default='ggggg', upload_to=apps.feitube.models.get_file_path_videos),
            preserve_default=False,
        ),
    ]
