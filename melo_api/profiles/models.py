from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Profile(models.Model):
    STATUS = [("BM", "Looking for bandmembers"), ("LB", "Looking for band")]

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    subname = models.CharField(max_length=255, blank=True, null=True)
    contact_info = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="images/", default="../default_profile_opkx3m")
    country = CountryField()
    status = models.CharField(max_length=2, choices=STATUS, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_joined"]

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
