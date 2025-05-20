"""
This is a simple ecommerce store  api which acts as a bridge between Frontend and Database

Framework used : Django Rest Framework
Funtions:
 -> Allows super user to add product
 -> Allows user to view the product
 -> Allows user to add, update or remove product from cart
 -> Allows user to place order or remove order
 -> Allows user to view cart and order
 -> Provides Authentication to protect a users data
 
 language used : Python
 

"""







import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.sessions.models import Session
from rest_framework.decorators import api_view
from rest_framework.response import Response
import re
"""
API: login, logout and register the user
this is used to register, log in the user and then log out the user 
 1) register user: registers user with, username, password and email
                  It also checks if the user already exist based on the email
 2)login and logout: this are used to log in the user and log out the user
 3) A user must follow this process to use any other api
"""
@csrf_exempt
@api_view(['POST'])
def register_user(request):
  data = request.data
  pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
  if re.match(pattern, data['email']):
    raise Exception("email id not valid")
  
  if len(data['password']) < 8:
    raise Exception("password be more than 8 letters")
  
  if User.objects.filter(email = data['email']).exists():
    return Response({"message":"user already exists"},status=404)
  else:
    user = User.objects.create_user(username = data['username'], password = data['password'], email = data['email'])
    login(request,user)
    return Response({"message":"user created and logged in"},status=200)
  
  
@csrf_exempt 
@api_view(['POST']) 
def login_user(request):
  data = json.loads(request.body)
  # user = User.objects.filter(username = data['username'], password = data['password']).first()
  user  = authenticate(username = data['username'], password=data['password'])
  if not user:
    return Response({"message":"user does not exist"},status=404)
  else:
    login(request,user)
    session_k = Session.objects.get(pk = request.session.session_key)
    return Response({"message":session_k.get_decoded()},status=200)
    
@login_required
@csrf_exempt
@api_view(['POST'])
def logout_user(request):
  logout(request)
  return Response({"message":"user logged out successfully"},status=200)
  
    
     
 