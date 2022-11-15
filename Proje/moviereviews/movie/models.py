from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/static/images/')
    url = models.URLField(blank=True)

class Uyelik(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

class Program(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)

def __str__(self):
    return self.title