from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from instruments import instruments


class Instrument(models.Model):
    LEVEL = [
        ("NO", "Novice"),
        ("IM", "Intermediate"),
        ("AV", "Advanced"),
        ("SP", "Semi-Professional"),
        ("PR", "Professional"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    instrument = models.CharField(
        choices=instruments.INSTRUMENTS, max_length=3, default="272"
    )
    experience = models.CharField(choices=LEVEL, max_length=2, default="PR")
    created_at = models.DateTimeField(auto_now_add=True)


def create_instrument(sender, instance, created, **kwargs):
    if created:
        Instrument.objects.create(owner=instance)


post_save.connect(create_instrument, sender=User)
