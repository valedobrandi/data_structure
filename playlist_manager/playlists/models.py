from django.db import models
from playlists.validators import validate_music_length

# Create your models here.


class Singer(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    musics = models.ManyToManyField("Music", related_name="playlists")

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=50)
    recorded_at = models.DateField()
    length_in_seconds = models.IntegerField(
        validators=[validate_music_length]
        )
    singer = models.ForeignKey(
        Singer,
        on_delete=models.CASCADE,
        related_name="musics",
        default=1    
    )

    def __str__(self):
        return self.name
