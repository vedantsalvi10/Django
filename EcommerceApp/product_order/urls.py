
from django.contrib import admin
from django.urls import path
from product_order import views

urlpatterns = [
   path('order_specific_product/', views.order_specific_product, name = "order_specific_product"),
   path('order_cart/', views.order_cart, name = "order_cart")
]