from django.db import models
from datetime import datetime
from django.db.models.base import Model
from django.utils import timezone

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Picture(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    perks = models.IntegerField(default=0)
    created = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ['-perks']

    def __str__(self):
        return self.title + ' from ' + self.album.title
