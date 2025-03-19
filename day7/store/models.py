from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateField()
  expired_at = models.DateField()
  description = models.TextField(max_length=255, default=None)
  price = models.DecimalField(max_digits=8,decimal_places=2)

class Store(models.Model):
  product = models.ForeignKey(Product, on_delete= models.CASCADE)
  qty = models.IntegerField()
  shell_date = models.DateField()
  store_name = models.CharField(max_length=255, default=None)
  