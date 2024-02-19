from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price =models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image_1=models.ImageField(upload_to='products', blank=True)

    def __str__(self):
        return self.name