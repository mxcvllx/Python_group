from django.db import models


class ContactUs(models.Model):
    country = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    street = models.CharField(max_length=255)
    location = models.CharField(max_length=300, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.country

