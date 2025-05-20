
from django.contrib.auth.models import User
from .serializers import OrderSerializer
from django.views.decorators.csrf import csrf_exempt
from user_registraion.models import Product
from cart.models import Cart
from .models import Order
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response

"""
API: order create, view
order has two views:
1) to place for the entire cart
2) to place order for a specific_product

1) order:
It has 3 request call: "POST","GET","DELETE"
It itterates through the entire cart for a particular user and places order for each product
models used: Cart, User, Order
serializer used: OrderSerializer
"""
"""
2)order_specific_product:
It places order for a specific user. It is used when the user does not want to use cart
requests called: "POST","GET","DELETE"
models used: User, Order
serializer used : OrderSerializer
"""
@login_required
@csrf_exempt
@api_view(["POST","GET","DELETE"])
def order(request):
  if request.method == "POST":
    user = User.objects.get(id = request.user.id)
    cart_product = Cart.objects.filter(user = user)
    for item in cart_product:
      product_order = Order.objects.create(
        User = user,
        Total_Price = item.total_price,
        qty = item.qty
      )
      product_order.Product.add(item.product)
  
  elif request.method == "DELETE":
    item = Order.objects.get(id = id)
    item.delete()
  
  order = Order.objects.all()
  if not order:
    return Response({"message":"no order placed"},status = 200)
  serialize_order = OrderSerializer(order, many = True).data
  return Response(serialize_order, status = 200)
  
@login_required
@csrf_exempt
@api_view(["POST","GET","DELETE"])
def order_specific_product(request, id = 3):
  if request.method == "POST":
    data = request.data
    user = User.objects.get(id = request.user.id)
    product = Product.objects.get(id= data["product_id"])
    product_order = Order.objects.create(
        User = user,
        qty = data['qty'],
        Total_Price = product.Price * data["qty"],
      )
    product_order.Product.add(product)
  elif request.method == "DELETE":
    item = Order.objects.get(id = id) #the id will be passed in the parameters insted of request.data
    item.delete()
  order = Order.objects.filter(User__id = request.user.id)
  if not order:
    return Response({"message":"no order placed"},status = 200)
  serialize_order = OrderSerializer(order, many = True).data
  return Response(serialize_order, status = 200)