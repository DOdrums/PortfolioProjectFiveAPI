# Generated by Django 3.2.16 on 2023-01-16 13:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Song',
            new_name='Follower',
        ),
    ]
