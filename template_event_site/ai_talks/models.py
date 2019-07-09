from django.db import models

# Create your models here.


class Speaker(models.Model):
    name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    bio = models.TextField()
    abstract = models.TextField()
    image_path = models.CharField(max_length=300)
    date_and_time = models.CharField(max_length=300)
    talk_location = models.CharField(max_length=300)
    talk_title = models.CharField(max_length=300)
