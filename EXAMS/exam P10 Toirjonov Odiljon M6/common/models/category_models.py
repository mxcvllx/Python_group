from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    position = models.PositiveSmallIntegerField(default=0)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children", null=True, blank=True)

    def __str__(self):
        return self.title

    def sav(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.title.upper():
            self.slug = slugify(self.title.lower())
        self.slug = slugify(self.title)
        return super().save(force_insert, force_update, using, update_fields)


class Brand(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="brands", null=True)

    def __str__(self):
        return self.title
