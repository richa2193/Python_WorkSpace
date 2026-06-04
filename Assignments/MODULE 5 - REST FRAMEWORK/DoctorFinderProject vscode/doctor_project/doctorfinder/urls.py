from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import RegisterView, book_appointment, user_dashboard
from .views import doctors_page
from .views import create_payment

from .views import (
    DoctorViewSet,
    AppointmentViewSet,
    home
)


from .views import (
    home,
    doctors_page,
    appointments_page,
    dashboard,
    doctor_detail
)

router = DefaultRouter()

router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', home, name='home'),

    path(
        'api/register/',
        RegisterView.as_view(),
        name='register'
        ),

    path('api/', include(router.urls)),

    path(
        'doctors/',
        doctors_page,
        name='doctors'
        ),

    path(
        'appointments/',
        appointments_page,
        name='appointments_page'
        ),

    path(
        'api/',
        include(router.urls)
        ),

    path(
        'dashboard/',
        dashboard,
        name='dashboard'
        ),

    path(
        'doctor/<int:id>/',
        doctor_detail,
        name='doctor_detail'
        ),

    path(
        'book/<int:doctor_id>/',
        book_appointment,
        name='book_appointment'
        ),

    path(
        'my-dashboard/',
        user_dashboard,
        name='user_dashboard'
    ),

    path(
        'create-payment/',
        views.create_payment,
        name='create_payment'
    ),

]