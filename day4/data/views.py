"""
API:
1) profiles/              view: profile_view
2) profiles/{id}          view: specific_profile
  """

from django.shortcuts import render,redirect,get_object_or_404
from data.models import Profile
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, re
# Create your views here.
 
@csrf_exempt
def profile_view(request):
  """
  API : profile/
    
    objective: Retrive and Create Profiles 
    Methods used: POST and GET
    
    POST:
    objective: creates a profile containing name, email, mobile number and address
    status: 201
    Exceptions: handles emty name and email and validates email
    variables: data (contains request.body)
               valid (validates email)
               proifile_obj (creates the creates profile)
               remodel_data (contains dict version of profile_obj)
    GET:
    objective: Used to retrive all the profiles from the database and returns to a list of profiles
    status:201
    Exception: handles methods other then GET and POST
     variables: data (contains list of profile values)
                profiles (contails data from PROFILE table)
                  
  """
  if request.method == "POST":
    data = json.loads(request.body)
    if not data["name"] or not data["email"]:
      raise Exception("Enter a valid name and email")
    valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', data["email"])
    if not valid:
      raise Exception("enter a valid mail id ") 
    profile_obj = Profile.objects.create(
      name = data["name"],
      email = data["email"],
      mobile_number = data["mobile_number"],
      address = data["address"]
    )
    remodel_data = model_to_dict(profile_obj) 
    return JsonResponse(remodel_data, status=201)

  elif request.method == "GET":
    profiles= Profile.objects.all()
    data = list( profiles.values())
    return JsonResponse(data, safe=False)
  else:
    return JsonResponse({"message": "invalid method call"}, status=404)
  
  
@csrf_exempt
def specific_profile(request, id):
  """
  API: profiles/{id}/
  
  objective: checks if the id matches the data, Retrive, Update and Delete the proflie.
  methods used: PUT,GET,DELETE
  
  PUT:
  objective: updates required data for a id. 
  status: 200
  Exception: returns status 404 if id is not found.
  variables: profile ( contains data from PROFILE table in database)
             updated_data( contains data from request.body)
             remodeled_profile(contains dict version of profile)
  
  DELETE:
  objective: deltes the profile at the specific id
  status:200
  Exception: returns status 404 if id not found
  variables: profile ( contains data from PROFILE table in database)
  
  GET:
  objective: retrives data for a specific id
  status: 201
  Exception: returns status 404 if id not found
  variables: profile ( contains data from PROFILE table in database)
             remodeled_profile(contains dict version of profile)
  
  Exception: hadles other methods.
  """
  if request.method == "PUT":
    profile = get_object_or_404(Profile, id=id)
    updated_data = json.loads(request.body)
    profile.name = updated_data.get("name", profile.name)
    profile.email = updated_data.get("email", profile.email)
    profile.mobile_number = updated_data.get("mobile_number", profile.mobile_number)
    profile.address = updated_data.get("address", profile.address)
    profile.save()
    remodeled_profile = model_to_dict(profile)
    return JsonResponse(remodeled_profile, status=200)
  elif request.method == "DELETE":
    profile = get_object_or_404(Profile, id=id)
    profile.delete()
    return JsonResponse({"message": "Profile deleted successfully !!"} , status = 200)
  elif request.method == "GET":
    profile = get_object_or_404(Profile, id=id)
    remodel_profile = model_to_dict(profile)
    return JsonResponse(remodel_profile, status=201)
  else:
    return JsonResponse({"message": "Invalid method for this api"}, status= 404) 