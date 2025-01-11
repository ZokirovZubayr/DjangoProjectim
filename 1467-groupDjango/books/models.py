from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=1000)


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    count = models.IntegerField()


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    color = models.CharField(max_length=100)
    speed = models.CharField(max_length=100)

    def __str__(self):
        return self.car_name


class Choice(models.Model):
    COLORS = [
        ("R", "RED"),
        ("G", "GREEN"),
        ("B", "BLUE"),
    ]

    colors = models.CharField(max_length=1, choices=COLORS)