from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.
fs = FileSystemStorage(location='/var/www/robopod/media')


class Author (django.db.models.Model):
    title = django.db.models.CharField(max_length=200)
    description = django.db.models.CharField(max_length=1000)


class Podcast(django.db.models.Model):
    author = django.db.models.ForeignKey(Author, on_delete=django.db.models.CASCADE)
    podcast_title = django.db.models.CharField(max_length=1000)
    podcast_description = django.db.models.CharField(max_length=1000)
    podcast_image = django.db.models.ImageField(fs)


class PodcastEpisode(django.db.models.Model):
    episode_title = django.db.models.CharField(max_length=200)
    publicated = django.db.models.DateField()
    pod_description = django.db.models.CharField(max_length=1000)
    podcast_file = django.db.models.FileField(fs)
    podcast = django.db.models.ForeignKey(Podcast, on_delete=django.db.models.CASCADE)
