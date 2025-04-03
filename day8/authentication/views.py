from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
@csrf_exempt
def register_user(request):
  if request.method == "POST":
   
   data = json.loads(request.body)
   print(data['username'])
   name = data['username']
   special_characters = '!@#$%^&*()_-+=][}{;:<>,./?'
   for char in name:
     if char in special_characters:
       return JsonResponse({'message': 'Username contains special characters'}, status = 400)
  #  if any(char in special_characters for char in name):
  #       return JsonResponse({'message': 'Username contains special characters'})
   if data["username"] == "":
     return JsonResponse({"message": "username an not be empty"}, status=400)
   elif len(data['password']) < 8:
     return JsonResponse({"message": "password should be of minimum 8 characters"}, status=400)
   elif User.objects.filter(username=data['username']).exists():
     return JsonResponse({"message": "user already exist"}, status=400)
   else:
     User.objects.create(username = data['username'], password= data['password'])
     return JsonResponse({"success": "Account successfully created!"}, status=200)
  else:
    return JsonResponse({"message": "invalid method"}, status=404) 

@csrf_exempt  
def login_user(request):
  if request.method == "POST":
   data = json.loads(request.body)
   print(data["username"], data["password"])
  #  user = authenticate(request, username= data["username"], password = data["password"])
   user = User.objects.filter(username = data["username"],password = data["password"]).first()
   print(user)
   if user is None: 
     return JsonResponse({"failed" : 'username or password is incorrect'}, status=404)
   else:
     login(request,user)
     request.session.save()
     return JsonResponse({"success": "logged in successfully", "session key": request.session.session_key}, status=200)

    
  else: 
    return JsonResponse({'message': "invalid method"}, status=404)
  
@csrf_exempt  
def logout_user(request):
  logout(request)
  return JsonResponse({'message':"user logged out"})
@csrf_exempt  
@login_required
def protected_view(request):
  return JsonResponse({"message": "userlogged in successfully"}, status= 200)
  