# Generated by Django 3.2.16 on 2023-01-06 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-date_joined']},
        ),
    ]
