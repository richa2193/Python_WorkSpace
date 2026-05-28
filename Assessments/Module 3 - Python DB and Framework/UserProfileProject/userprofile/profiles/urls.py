from django.urls import path
from . import views

urlpatterns = [

    path('', views.create_profile, name='create_profile'),

    path('profiles/', views.profile_list, name='profile_list'),

]