from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)


class Music(models.Model):
    artist = models.CharField(max_length=30)
    album = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.artist} - {self.album}"


