from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=1, unique=True)
    price = models.IntegerField()

class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    discounted_price = models.IntegerField()
