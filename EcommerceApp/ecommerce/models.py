from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
  Title = models.CharField(max_length=50)
  Description = models.TextField()
  Price = models.DecimalField(max_digits=11,decimal_places=2)
  Image = models.ImageField(upload_to='product_images')