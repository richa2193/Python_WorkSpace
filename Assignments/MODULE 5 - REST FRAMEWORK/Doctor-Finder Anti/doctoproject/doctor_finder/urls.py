from django.urls import path
from . import views
from .views import DoctorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctor')

urlpatterns = router.urls
