from django.shortcuts import render
from .models import *
from .serializers import *

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])

def getall(request):

    data = studinfo.objects.all()

    serial = studserializer(data,many=True)

    return Response(serial.data)