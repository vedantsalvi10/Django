from rest_framework import serializers
from ..user_registraion.models import Product

class ProductSerialize(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'
