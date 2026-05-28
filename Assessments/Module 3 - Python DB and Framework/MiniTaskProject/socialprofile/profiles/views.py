from django.shortcuts import render,redirect
from .models import profile
from .forms import ProfileForm
import csv
from django.http import HttpResponse
# Create your views here.

def create_profile(request):

    if request.method == 'POST':

        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        age = request.POST.get('age')
        bio = request.POST.get('bio')

        profile.objects.create(
            fullname=fullname,
            email=email,
            age=age,
            bio=bio
        )

        return redirect('/')

    return render(request, 'create_profile.html')


def profile_list(request):

    profiles = profile.objects.all()

    return render(request, 'profile_list.html', {'profiles': profiles})


def export_profiles(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="profiles.csv"'

    writer = csv.writer(response)

    writer.writerow(['fullname', 'email', 'age', 'bio'])

    profiles = profile.objects.all()

    for p in profiles:

        writer.writerow([
            profile.fullname,
            profile.email,
            profile.age,
            profile.bio
        ])

    return response