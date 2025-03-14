from django.shortcuts import render,redirect
from dataEntry.models import Profile
# Create your views here.
def profileView(request):
  if request.method == 'POST':
    name = request.POST.get('name','')
    Profile.objects.create(name=name)
    return redirect("profile")
  else:
    stored_names = Profile.objects.all()
    context = {'stored_names':stored_names}
    return render(request,'profile.html',context)