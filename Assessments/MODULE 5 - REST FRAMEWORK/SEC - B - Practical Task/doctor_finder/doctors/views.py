from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Doctor
from django.db import transaction
from django.db import transaction
from .serializers import DoctorSerializer
from .pagination import DoctorPagination

# Create your views here.

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['name', 'specialization', 'city']
    ordering_fields = ['name', 'specialization', 'city', 'experience']

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
def home(request):
    return render(request, "home.html")