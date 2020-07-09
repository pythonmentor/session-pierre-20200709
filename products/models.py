from django.db import models

from .managers import ProductManager


# Create your models here.
class Product(models.Model):
    name = models.CharField("product name")

    objects = ProductManager()
