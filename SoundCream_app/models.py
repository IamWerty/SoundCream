from django.db import models
from account_app.models import CustomUser

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='songs')
    length = models.PositiveIntegerField()
    rates = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    matching_song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    rates = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Playlist(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_playlists')
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    songs = models.ManyToManyField(Song, blank=True, related_name='playlists')
    rates = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
