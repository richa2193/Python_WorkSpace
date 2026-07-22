from django.shortcuts import render, redirect
from .forms import * 
from .models import *
import requests 

# Create your views here.
def index(request):
    if request.method=="POST":
        form=studinfo(request.POST)
        if form.is_valid():
            form.save()
            print("Record Inserted!")
        else:
            print(form.errors)

    return render(request, 'index.html')

def showdata(request):
    stdata=studform.objects.all()
    return render(request, 'showdata.html', {'stdata': stdata})

def updatedata(request, id):
    stid=studform.objects.get(id=id)
    if request.method=='POST':
        form=studinfo(request.POST, instance=stid)
        if form.is_valid():
            form.save()
            print("Record Updated!")
            return redirect('showdata')
        else:
            print(form.errors)
    return render(request, 'updatedata.html', {'stid': stid})

def deletedata(request, id):
    stid=studform.objects.get(id=id)
    studform.delete(stid)
    return redirect('showdata')

# username = richu
# password = test@123