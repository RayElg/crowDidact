from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=150)

class Blurb(models.Model):
    blurbText = models.TextField(max_length=5000)
    fromLink = models.URLField(max_length=600)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="blurb")

class YoutubeVideo(models.Model):
    link = models.URLField(max_length=600)
    favorites = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class LectureNote(models.Model):
    title = models.CharField(max_length=80,default="Note")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    favorites = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)