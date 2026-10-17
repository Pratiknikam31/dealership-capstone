from django.db import models
from django.contrib.auth.models import User

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.year} {self.car_make.name} {self.name}"

class Dealer(models.Model):
    full_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address = models.TextField()
    zip = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()
    short_name = models.CharField(max_length=100)
    st = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

class Review(models.Model):
    dealership = models.IntegerField()
    name = models.CharField(max_length=200)
    purchase = models.BooleanField(default=False)
    review = models.TextField()
    purchase_date = models.DateField(blank=True, null=True)
    car_make = models.CharField(max_length=100, blank=True)
    car_model = models.CharField(max_length=100, blank=True)
    car_year = models.IntegerField(blank=True, null=True)
    sentiment = models.CharField(max_length=20, blank=True)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return f"Review by {self.name} for dealership {self.dealership}"
