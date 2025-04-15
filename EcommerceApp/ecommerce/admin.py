from django.contrib import admin
from ecommerce.models import Product
from product_cart.models import Cart
from product_order.models import Order
# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
