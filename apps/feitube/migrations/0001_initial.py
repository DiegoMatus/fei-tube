# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import apps.feitube.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Título', max_length=255)),
                ('amount', models.IntegerField(verbose_name='Cantidad')),
            ],
            options={
                'verbose_name_plural': 'Playlists',
                'verbose_name': 'Playlist',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('facebook', models.URLField(verbose_name='Facebook', max_length=255)),
                ('twitter', models.URLField(verbose_name='Twitter', max_length=255)),
                ('instagram', models.URLField(verbose_name='Instagram', max_length=255)),
                ('google', models.URLField(verbose_name='Google +', max_length=255)),
                ('profile_picture', models.FileField(upload_to=apps.feitube.models.get_file_path_profiles)),
                ('cover_picture', models.FileField(upload_to=apps.feitube.models.get_file_path_covers)),
                ('slug', models.SlugField(null=True, blank=True, max_length=255, unique=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Perfiles',
                'verbose_name': 'Perfil',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('score', models.IntegerField(verbose_name='Calificación')),
                ('profile', models.ForeignKey(to='feitube.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Título', max_length=255)),
                ('description', models.TextField(verbose_name='Descripción')),
                ('views', models.IntegerField(verbose_name='Visitas')),
                ('tags', models.CharField(verbose_name='Tags', max_length=255)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('favs_count', models.IntegerField(verbose_name='Favoritos')),
                ('slug', models.SlugField(null=True, blank=True, max_length=255, unique=True)),
                ('favs', models.ManyToManyField(to='feitube.Profile', related_name='videos_fav')),
                ('profile', models.ForeignKey(to='feitube.Profile', related_name='videos', verbose_name='Usuario')),
                ('rates', models.ManyToManyField(to='feitube.Profile', through='feitube.Rate', related_name='videos_rate')),
            ],
            options={
                'verbose_name_plural': 'Videos',
                'verbose_name': 'Video',
            },
        ),
        migrations.AddField(
            model_name='rate',
            name='video',
            field=models.ForeignKey(to='feitube.Video'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='profile',
            field=models.ForeignKey(to='feitube.Profile', related_name='playlist', verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='videos',
            field=models.ManyToManyField(to='feitube.Video'),
        ),
    ]
