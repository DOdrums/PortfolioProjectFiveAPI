from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from song.models import Song


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
