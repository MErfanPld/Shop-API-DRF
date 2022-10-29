from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    discription = models.TextField()
    price = models.FloatField()
    # image = models.ImageField(default='1.png')

    def __str__(self):
        return self.name
