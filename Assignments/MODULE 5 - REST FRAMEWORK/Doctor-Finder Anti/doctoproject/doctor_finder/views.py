from rest_framework import viewsets, permissions
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    """API endpoint that allows doctors to be viewed or edited.

    Uses Django REST Framework's ModelViewSet to provide `list`, `retrieve`,
    `create`, `update`, and `destroy` actions. Authentication is optional for
    read‑only access and required for modifying data.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
