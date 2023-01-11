from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    audio = models.FileField(upload_to="songs/", default="../rock_it_pycp3h")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
