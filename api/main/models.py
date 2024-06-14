from django.db import models

# Create your models here.
gender = (("male", "male"), ("female", "female"))


class People(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(
        default="choose your gender", choices=gender, max_length=50)

    age = models.IntegerField()

    def __str__(self):
        return self.name


class Car(models.Model):
    car_name = models.CharField(max_length=50)
    speed = models.CharField(max_length=50)

    def __str__(self):
        return self.car_name
