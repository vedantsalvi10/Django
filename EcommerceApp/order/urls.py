
from django.contrib import admin
from django.urls import path
from order import views

urlpatterns = [
   path('order_specific_product/', views.order_specific_product, name = "order_specific_product"),
   path('order/', views.order, name = "order")
] 