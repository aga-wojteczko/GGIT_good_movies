from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    published_at = models.DateTimeField()

def __str__(self):
    return "Film: " + self.title


# Create your models here.
