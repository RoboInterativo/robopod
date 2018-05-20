from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.
fs = FileSystemStorage(location='/var/www/robopod/')

class Author (models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)


class Podcast(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    podcast_title = models.CharField(max_length=1000)


class PodcastEpisode (models.Model):
    episode_title=models.CharField(max_length=200)
    publicated=models.DateField()
    pod_description=models.CharField(max_length=1000)
    podcast_file=models.FileField(fs)
    podcast = models.ForeignKey(Podcast,on_delete=models.CASCADE)
