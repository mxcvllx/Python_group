from django.db import models


class Pallets(models.Model):
    title = models.CharField('title', max_length=100)
    description = models.TextField()
    price = models.FloatField(unique=True)
    image = models.ImageField()
