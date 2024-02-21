from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

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
    dealer_id = models.IntegerField() 
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES)
    year = models.DateField()

    def __str__(self):
        return f"{self.year} {self.make.name} {self.name}"

class DealerReview(models.Model):
    dealership = models.ForeignKey(CarDealer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    purchase = models.BooleanField()
    review = models.TextField()
    purchase_date = models.DateField()
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.DateField()
    sentiment = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Review for {self.dealership}: {self.review}"
