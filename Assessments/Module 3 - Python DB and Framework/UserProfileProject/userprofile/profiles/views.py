from django.shortcuts import render,redirect
from .forms import userprofileform
from .models import userprofile

# Create your views here.
def create_profile(request):
    if request.method=="POST":
        form=userprofileform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = userprofileform()

    return render(request, 'create_profile.html',{'form':form})

#display profile 
def profile_list(request):
    profiles=userprofile.objects.all()
    return render(request,'profile_list.html', {'profiles':profiles})