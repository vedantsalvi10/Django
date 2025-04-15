from django.contrib import admin
from django.urls import path
from product_cart import views

urlpatterns = [
      path('cart/',views.cart, name='cart')
]