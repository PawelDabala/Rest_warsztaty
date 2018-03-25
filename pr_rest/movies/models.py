from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=124)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=124)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name="director")
    actors = models.ManyToManyField(Person, through="Movie_Characters")
    year = models.IntegerField()

    def __str__(self):
        return self.title

class Movie_Characters(models.Model):
    persons = models.ForeignKey(Person)
    movies = models.ForeignKey(Movie)
    role = models.CharField(max_length=124)

    def __str__(self):
        return self.role
