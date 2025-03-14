from django.shortcuts import render,redirect,get_object_or_404
from dataEntry.models import Profile
from django.http import HttpResponse
import re

# for url profile (can enter and view profile)
def profileView(request):
  if request.method == "POST":
     name = request.POST.get("name",'')
     contact = request.POST.get("contact",'')
     address = request.POST.get("address",'')
     department = request.POST.get("department")
     if not name or not contact or not address or not department:
       raise Exception("Fill all the fields before submiting")
     if len(contact) >10:
       raise Exception("the contact number is invalid!!")
     Profile.objects.create(name=name,contact=contact,address=address,department=department)
     return redirect('profile')
  else:
     stored_data = Profile.objects.all()
     context = {'stored_data': stored_data}
     return render(request,'profile.html',context)

  #  used when a person wants to view one specific profile. Uses Id to get a profile
def singleProfile(request, id):
    data = get_object_or_404(Profile, id=id)
    context = {'data':data}
    return render(request,'name.html',context)

#  it is used to add or update a profiles email id. 
def update_email(request, id):
  if request.method == "POST":
    profile = get_object_or_404(Profile, id=id)
    email = request.POST.get("email","")
    valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    if not valid:
      raise Exception("enter valid email Id")
    profile.email = email
    profile.save()
    return redirect('singleProfile', id=id)
  else:
    data = get_object_or_404(Profile, id=id)
    context = {"data":data}
    return render(request,'email.html',context)