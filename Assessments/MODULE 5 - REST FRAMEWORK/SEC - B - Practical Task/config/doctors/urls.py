from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet
from .views import home

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)

urlpatterns = [
    path("", home),
]


urlpatterns += router.urls