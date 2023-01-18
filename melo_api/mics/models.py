from django.db import models
from django.contrib.auth.models import User
from song.models import Song


class Mic(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
