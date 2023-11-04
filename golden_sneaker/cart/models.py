from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Product(models.Model):
    image = RichTextField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    