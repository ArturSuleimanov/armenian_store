from django.db import models


# Create your models here.
class Product(models.Model):
    in_stock = models.BooleanField(default=True)
    name = models.TextField(max_length=100, default="")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default="photos/default.png")
    description = models.TextField(max_length=1024, default="")
    composition = models.TextField(max_length=1024)
    nutritional_value = models.TextField(max_length=512)
    weight = models.IntegerField(default=0)
    price = models.IntegerField(default=0)


