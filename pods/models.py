from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.
fs = FileSystemStorage(location='/var/www/robopod/media')


class Author (models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default='')

    def __str__(self):
        return '{} '.format(self.title)


class Podcast(models.Model):
    author = models.ForeignKey(Author,related_name='Author', on_delete=models.CASCADE)
    podcast_title = models.CharField(max_length=1000)
    podcast_description = models.CharField(max_length=1000, default='')
    podcast_image = models.ImageField(fs)

    def __str__(self):
        return '{} -{}'.format(self.podcast_title,self.podcast_description)


class PodcastEpisode(models.Model):
    episode_number=models.IntegerField(default=0)
    episode_title = models.CharField(max_length=200)
    publicated = models.DateField()
    pod_description = models.CharField(max_length=1000, default='')
    podcast_file = models.FileField(fs)
    podcast = models.ForeignKey(Podcast,related_name='Podcast', on_delete=models.CASCADE)

    def __str__(self):
        return '{} -{}'.format(self.episode_title,self.pod_description)
