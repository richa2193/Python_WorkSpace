from django.contrib import admin
from .models import *

# Register your models here.
class stdata(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','name','email','dob','mobile']


admin.site.register(studinfo,stdata)

