from django.contrib import admin
from django.urls import path
from products_view import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product_view/', views.product_view, name = "product_view"),
    path('product_view/<int:id>/',views.specific_product, name = 'specific_product'),
    
]