from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to="media/products", null=True, blank=True
    )

    def __str__(self):
        return f'{self.name} - {self.price}'


class Customers(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
