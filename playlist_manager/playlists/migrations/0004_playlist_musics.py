# Generated by Django 5.1.2 on 2024-10-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0003_music_singer'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='musics',
            field=models.ManyToManyField(related_name='playlists', to='playlists.music'),
        ),
    ]
