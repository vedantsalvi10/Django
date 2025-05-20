from django.contrib import admin
from user_registraion.models import Product
from cart.models import Cart
from order.models import Order
# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
