from django.db import models


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # You can include any other fields you want here

    def __str__(self):
        return self.name


class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()  # Refers to a dealer created in Cloudant database
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES)
    year = models.DateField()
    # You can include any other fields you want here

    def __str__(self):
        return f"{self.year} {self.make.name} {self.name}"
