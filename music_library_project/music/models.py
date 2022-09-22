from django.db import models

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length = 250)
    artist = models.CharField(max_length = 250)
    album = models.CharField(max_length = 400)
    release = models.DateField(max_length = 400)
    genre = models.CharField(max_length = 400)