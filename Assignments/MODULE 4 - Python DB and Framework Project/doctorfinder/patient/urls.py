from django.urls import path
from . import views

urlpatterns = [
    path('', views.register),
    # path('login/', views.login),
    # path('doctors/', views.doctors),
    # path('about/', views.about),
    # path('contact/', views.contact),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('profile/', views.profile),

]