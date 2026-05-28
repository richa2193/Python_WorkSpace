from django.urls import path
from .views import index
from . import views

urlpatterns = [

    path('', index),
    path('', views.doctor_home),

    path('add/', views.add_doctor),
    path('update/<int:id>/', views.update_doctor),

    path('delete/<int:id>/', views.delete_doctor),

]