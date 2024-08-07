from django.db import models

# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=100)
    carModel = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.make + ' ' + self.carModel


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    rating = models.IntegerField(max_length=2)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car} {self.author} {self.rating}"