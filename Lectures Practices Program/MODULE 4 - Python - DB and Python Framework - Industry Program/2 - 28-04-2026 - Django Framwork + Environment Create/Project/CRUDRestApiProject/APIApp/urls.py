from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index),
    path('getdata/',views.getdata),
    path('searchdata/<int:id>/',views.searchdata),
    path('savedata/',views.savedata),
    path('updatedata/<int:id>/',views.updatedata),
    path('deletedata/<int:id>/',views.deletedata),
    path('',views.index),
]