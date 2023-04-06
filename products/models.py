from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class user(models.Model):
    f_name = models.CharField(max_length=10)
    l_name = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length= 100)
    username = models.CharField(max_length=20)
    password = models.TextField(max_length=255 )

