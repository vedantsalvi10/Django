import json
# the model and serializer for the product is in the ecommerce app
from ecommerce.serializers import ProductSerialize
from django.views.decorators.csrf import csrf_exempt
from ecommerce.models import Product
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

"""
API: 1) product_view: this api allows user to view all the products.
        It does not require the user to login 
     2) specific product: this is used to go on a specific product with the help of id

Products can be added from admin by super user, this allows the user to only view the product,
or add to cart or place order for the product.


"""
@login_required
@csrf_exempt
@api_view()
def product_view(request):
  product = Product.objects.all()
  if not product:
    return Response({"message":"no products added"},status=404)
  serializer = ProductSerialize(product,many = True)
  return Response(serializer.data,status=200)

  
"""
API: specific product: this is used to go on a specific product with the help of id

"""
@login_required
@csrf_exempt
@api_view()
def specific_product(request, id):
  specific_product = Product.objects.filter(id=id)
  if not specific_product:
    return Response({"message":"product not found"},status=404)
  serialize = ProductSerialize(specific_product, many = True)
  return Response(serialize.data,status=200)
