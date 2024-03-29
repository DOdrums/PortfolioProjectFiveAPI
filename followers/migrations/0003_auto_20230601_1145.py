# Generated by Django 3.2.16 on 2023-06-01 11:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followers', '0002_rename_song_follower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follower',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together={('owner', 'followed')},
        ),
    ]
