# Generated by Django 5.1.2 on 2024-10-27 15:29

import playlists.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='length_in_seconds',
            field=models.IntegerField(validators=[playlists.validators.validate_music_length]),
        ),
    ]
