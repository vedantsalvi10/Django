from django.db import models
from django.contrib.auth.models import User
# from product_cart.models import Cart
from ecommerce.models import Product
# Create your models here.
class Order(models.Model):
  User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
  Product = models.ManyToManyField(Product, related_name='orders')
  qty = models.IntegerField()
  Total_Price = models.DecimalField(max_digits=15,decimal_places=2)
  Created_Date = models.DateTimeField(auto_now_add=True)
  