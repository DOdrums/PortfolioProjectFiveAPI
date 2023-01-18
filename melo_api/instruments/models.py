from django.db import models
from django.contrib.auth.models import User
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
    instrument = models.CharField(choices=instruments.INSTRUMENTS, max_length=3)
    experience = models.CharField(choices=LEVEL, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
