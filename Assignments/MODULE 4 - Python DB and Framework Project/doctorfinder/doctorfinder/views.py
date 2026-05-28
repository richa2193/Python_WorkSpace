from django.shortcuts import render
from doctor.models import doctor

def home(request):
    return render(request, 'home.html')

def profile(request):
    data=doctor.objects.all()
    return render(request, 'profile.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request,'about.html')