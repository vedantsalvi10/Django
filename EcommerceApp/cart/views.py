import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from user_registraion.models import Product
from .models import Cart
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .serializers import CartSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
"""
API: cart view, create, delete

cart:
It is used to add products in the cart, change the qty of the product in the
cart and remove them from cart
models used: Cart,Product,User
serializer used: CartSerializer

user is required to be logged in to use Cart
for delete parameter should be passed call product_id
"""
@login_required
@csrf_exempt
@api_view(['POST','PUT','DELETE','GET'])
def cart(request):
  # POST
  if request.method == "POST":
    data = request.data
    user = User.objects.get(id = request.user.id)
    product = Product.objects.get(id = int(data['product_id']))
    cart = Cart.objects.create(user = user, product = product, qty = int(data['qty']), total_price = int(data['qty']) * product.Price)
    serialized_cart = CartSerializer(cart)
    return Response(serialized_cart.data, status = 200)
  
  # PUT
  elif request.method == "PUT":
    data = json.loads(request.body)
    cart = Cart.objects.get(product__id = data['product_id'])
    cart.qty = data['qty']
    cart.total_price = cart.qty * cart.product.Price
    cart.save()
    serialized_cart = CartSerializer(cart)
    return Response(serialized_cart.data, status = 200)
  
   # Delete
  elif request.method == "DELETE":
    data = request.data
    cart = Cart.objects.get(product__id = data['product_id'])
    cart.delete()
    
  # view
  cart_products = Cart.objects.all()
  serialized_cart_products = CartSerializer(cart_products, many = True)
  return Response(serialized_cart_products.data)
  