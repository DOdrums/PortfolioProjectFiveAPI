from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from .validators import validate_audio


class Song(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    audio = models.FileField(
        upload_to="songs/",
        storage=VideoMediaCloudinaryStorage(),
        default="songs/rock_it_pycp3h",
        validators=[validate_audio],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
