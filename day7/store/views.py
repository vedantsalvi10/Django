from django.shortcuts import render
from store.models import Product,Store
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
# Create your views here.
@csrf_exempt
def store_view(request):
  if request.method == "POST":
    data = json.loads(request.body)
    product = Product.objects.create(
      name = data['name'],
      created_at = data['created_at'],
      expired_at = data['expired_at'],
      description = data['description'],
      price = data['price'],
    )
    store = Store.objects.create(
      product = product,
      qty = data['qty'],
      shell_date = data['shell_date'],
      store_name = data['store_name'],
    )
    remodel_store = model_to_dict(store)
    
    return JsonResponse(remodel_store, status=200)
  
  else:
    return JsonResponse({'message': 'another method'})