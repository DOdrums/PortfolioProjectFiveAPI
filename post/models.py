from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", default="../default_post_rgq6aq")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
