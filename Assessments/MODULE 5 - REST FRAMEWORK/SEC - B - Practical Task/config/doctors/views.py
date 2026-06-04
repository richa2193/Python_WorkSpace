from django.shortcuts import render
from django.db import transaction
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework import viewsets


# Create your views here.

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    #  Atomic Transaction (VERY IMPORTANT)
    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()

def home(request):
    doctors = Doctor.objects.all()
    return render(request, "home.html", {"doctors": doctors})