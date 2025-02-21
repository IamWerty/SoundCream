from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    follows = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='user_follows')
    Songs = models.ManyToManyField('SoundCream_app.Song', blank=True, related_name='user_songs')
    saved_playlists = models.ManyToManyField('SoundCream_app.Playlist', blank=True, related_name='users_who_saved_playlists')
    liked_songs = models.ManyToManyField('SoundCream_app.Song', blank=True, related_name='users_who_liked')
    liked_playlists = models.ManyToManyField('SoundCream_app.Playlist', blank=True, related_name='users_who_liked_playlists')

    def get_absolute_url(self):
        return reverse('user_profile')
