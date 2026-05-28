from django.shortcuts import get_object_or_404, render, redirect
from .models import doctor
from .forms import DoctorForm

# Create your views here.
def index(request):
    data = doctor.objects.all()
    return render(request,'doctor/index.html',{'data':data})

# doctor/views.py
def login(request):
    return render(request, 'patient/login.html')


# READ

def doctor_home(request):

    doctors = doctor.objects.all()

    return render(request, 'doctor/index.html', {'doctors': doctors})


# CREATE

def add_doctor(request):

    if request.method == 'POST':

        form = DoctorForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/doctor/')

    else:

        form = DoctorForm()

    return render(request, 'doctor/add_doctor.html', {'form': form})


# UPDATE

def update_doctor(request, id):

    doctor = get_object_or_404(doctor, id=id)

    if request.method == 'POST':

        form = DoctorForm(request.POST, instance=doctor)

        if form.is_valid():

            form.save()

            return redirect('/doctor/')

    else:

        form = DoctorForm(instance=doctor)

    return render(request, 'doctor/update_doctor.html', {'form': form})


# DELETE

def delete_doctor(request, id):

    doctor = get_object_or_404(doctor, id=id)

    doctor.delete()

    return redirect('/doctor/')