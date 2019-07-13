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
    sort = models.IntegerField()
    # def __str__(self):
        # return name


class Staff(models.Model):
    name = models.CharField(max_length=300)
    image_path = models.CharField(max_length=300)


class ScientificCommittee(models.Model):
    name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)


class StaticParts(models.Model):
    about = models.TextField()
    register_link = models.CharField(max_length=1000)
