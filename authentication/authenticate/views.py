from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import JsonResponse
# Create your views here.
@csrf_exempt
def register_user(request):
  if request.method == 'POST':
     data = json.loads(request.body)
     if User.objects.filter(username = data['username']).exists():
       return JsonResponse({"message":"user already exist"})
     else:
       User.objects.create(username = data['username'],password = data['password'])
       return JsonResponse({"message": "Accunt created succesfully"}, status=200)
  else:
    return JsonResponse({"message": "register the user"})

@csrf_exempt
def login_user(request):
     if request.method == 'POST':
         data = json.loads(request.body)
         user = User.objects.filter(username = data['username'],password = data['password']).first()
         if user is None:
           return JsonResponse({"message": "User does not exist"}, status= 404)
         else:
           login(request,user)
           return JsonResponse({"message": "user logged in successfully", "sessionKey": request.session.session_key}, status = 200)
     else:
       return JsonResponse({"message": "login the user"})
@csrf_exempt
@login_required
def home(request):
  return JsonResponse({"messaged":"user logged in"})