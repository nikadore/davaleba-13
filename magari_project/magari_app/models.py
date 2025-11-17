from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Person(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.surname}"
    


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.PositiveIntegerField()
    rating = models.FloatField(validators=[ MinValueValidator(0), MaxValueValidator(12)])

    def __str__(self):
        return f"{self.title} ({self.release_year})"
