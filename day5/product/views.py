from django.shortcuts import render
from product.models import Product
from django.http import JsonResponse
import json
from datetime import timedelta,date
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
# Create your views here.

@csrf_exempt
def product_view(request):
  """
  API: products/
       objective: TO CREATE PRODUCT in table and to retrive different type of products.
       methods used: POST and GET
       
       1) POST: 
           objective: to create product and return status 201
           variables: product (contains request.body)
                      product_obj(creates the object)
                      remodel_product (converts model to dictionary)
           Exception: none
      2) GET: 
      objective: retrive: all objects
                          objects in desc order by price
                          prodtucts created between specific dates
                          data from past 7 days
                          name with specific keywords
                          
           variables: products (contains products)
                      by_price(cotains values in desc order as per price)
                      by_date (includes products within certain range)
                      last_week_data(contains products from past 7 days)
                      by_keyword(contains products that has specific keyword in thier name)
           Exception: none
  """
  if request.method == "POST":
    product = json.loads(request.body)
    product_obj = Product.objects.create(
      name = product['name'],
      price = product['price'],
      description = product['description'],
      category = product['category']
    )
    product_obj.save()
    remodel_product = model_to_dict(product_obj)
    return JsonResponse(remodel_product, status=201)
  
  elif request.method == "GET":
    # getting all data
    products = list(Product.objects.all().values())

    
    # getting price by desc order
    by_price = list(Product.objects.order_by('-price').values())
    
    # getting products with created between specific range
    by_date = list(Product.objects.filter(created_at__range=("2025-03-16T14:58:35.671Z","2025-03-16T16:07:16.983Z")).values())
    
    # getting data from past 7 days
    d= date.today()-timedelta(days=7)
    last_week_data = list(Product.objects.filter(created_at__gte=d).values())
    
    # gwtting name with specific keyword
    by_keyword = list(Product.objects.filter(name__contains="o").values())
    return JsonResponse({"All_Products": products, "Ordered_by_price": by_price, "Ordered_by_date": by_date, "products_before_7days": last_week_data, "products_with_specifickeyword": by_keyword}, safe=False)