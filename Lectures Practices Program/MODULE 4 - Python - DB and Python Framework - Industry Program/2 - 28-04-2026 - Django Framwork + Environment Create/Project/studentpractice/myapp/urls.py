from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('showdata/', views.showdata, name='showdata'),
    path('deletedata/<int:id>', views.deletedata),
    path('updatedata/<int:id>', views.updatedata),
    
]