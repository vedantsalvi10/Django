from django.db import models
from django.contrib.auth.models import User
from ecommerce.models import Product
# Create your models here.


class Cart(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  qty = models.IntegerField()
  total_price = models.DecimalField(max_digits=15, decimal_places=2)
