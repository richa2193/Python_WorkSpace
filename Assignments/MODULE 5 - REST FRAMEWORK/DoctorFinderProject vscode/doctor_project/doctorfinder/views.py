from rest_framework import viewsets
from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegisterSerializer
from .email_service import send_email
import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import razorpay
from django.conf import settings


from .models import Doctor, Appointment
from .serializers import (
    DoctorSerializer,
    AppointmentSerializer
)
from .forms import AppointmentForm

def home(request):

    context = {

        'total_doctors':
        Doctor.objects.count(),

        'total_appointments':
        Appointment.objects.count(),

    }

    return render(
        request,
        'home.html',
        context
    )


class DoctorViewSet(viewsets.ModelViewSet):

    queryset = Doctor.objects.all().order_by('-id')

    serializer_class = DoctorSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = [
        'specialty',
        'city'
    ]

    search_fields = [
        'name',
        'specialty',
        'city'
    ]

    ordering_fields = [
        'name',
        'specialty',
        'city'
    ]


class AppointmentViewSet(viewsets.ModelViewSet):

    queryset = Appointment.objects.all().order_by('-id')

    serializer_class = AppointmentSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = [
        'status'
    ]

    search_fields = [
        'patient_name'
    ]

    ordering_fields = [
        'appointment_date'
    ]

class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer

    permission_classes = []

    def perform_create(self, serializer):

        user = serializer.save()

        send_email(
            subject="Welcome To Doctor Finder",
            message=f"""
Hello {user.username}

Your account has been created successfully.

Thank you for joining Doctor Finder.
""",
            recipient_email=user.email
        )

def create_payment(request):

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    payment = client.order.create({
        "amount": 50000,
        "currency": "INR",
        "payment_capture": 1
    })

    context = {
        "payment": payment,
        "razorpay_key": settings.RAZORPAY_KEY_ID,
        "amount": 50000,
    }

    return render(
        request,
        "payment.html",
        context
    )


def home(request):
    return render(request, 'home.html')


def doctors_page(request):

    doctors = Doctor.objects.all()

    search = request.GET.get('search')

    city = request.GET.get('city')

    specialty = request.GET.get('specialty')

    if search:
        doctors = doctors.filter(
            name__icontains=search
        )

    if city:
        doctors = doctors.filter(
            city__icontains=city
        )

    if specialty:
        doctors = doctors.filter(
            specialty__icontains=specialty
        )

    return render(
        request,
        'doctors.html',
        {
            'doctors': doctors
        }
    )

def appointments_page(request):

    appointments = Appointment.objects.select_related(
        'doctor'
    )

    return render(
        request,
        'appointments.html',
        {
            'appointments': appointments
        }
    )

def dashboard(request):

    context = {

        'doctor_count':
        Doctor.objects.count(),

        'appointment_count':
        Appointment.objects.count(),

        'user_count':
        User.objects.count(),

    }

    return render(
        request,
        'dashboard.html',
        context
    )

def doctor_detail(request, id):

    doctor = get_object_or_404(
        Doctor,
        id=id
    )

    return render(
        request,
        'doctor_detail.html',
        {
            'doctor': doctor
        }
    )

def book_appointment(request, doctor_id):

    doctor = Doctor.objects.get(
        id=doctor_id
    )

    appointment.user = request.user

    form = AppointmentForm()

    if request.method == 'POST':

        form = AppointmentForm(
            request.POST
        )

        if form.is_valid():

            appointment = form.save(
                commit=False
            )

            appointment.doctor = doctor

            appointment.save()

            return redirect(
                'appointments'
            )

    return render(
        request,
        'book_appointment.html',
        {
            'form': form,
            'doctor': doctor
        }
    )



@login_required
def user_dashboard(request):

    appointments = Appointment.objects.filter(
        user=request.user
    )

    return render(
        request,
        'user_dashboard.html',
        {
            'appointments': appointments
        }
    )