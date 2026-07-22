from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import student
from .serializers import studserial   
import requests 
# Create your views here.

# GET ALL DATA
@api_view(['GET'])
def getdata(request):
    Stud = student.objects.all()
    serial = studserial(Stud, many=True)
    return Response(serial.data)

#SEARCH SINGLE DATA 
@api_view(['GET'])  
def searchdata(request, id):
    try: 
        students = student.objects.get(id=id)

    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serial = studserial(students)

    return Response(serial.data)


#SAVE DATA  
@api_view(['POST'])
def savedata(request): 
    serial=studserial(data=request.data)

    if serial.is_valid():
        serial.save()

        return Response(
            {
                "message":"Data Inserted Successfully"
            },
            status=status.HTTP_201_CREATED
        )
    
    else:

        return Response(
            serial.errors,
            status=status.HTTP_404_NOT_FOUND
        )
    

@api_view(['GET', 'PUT'])
def updatedata(request, id):
    try:
        Stud = student.objects.get(id=id)

    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET Request
    if request.method == 'GET':
        serial = studserial(Stud)
        return Response(serial.data)

    # PUT Request
    elif request.method == 'PUT':
        serial = studserial(Stud, data=request.data)

        if serial.is_valid():
            serial.save()
            return Response({
                "message": "Data Updated Successfully"
            })

        return Response(serial.errors)


#DELETE DATA 
@api_view(['DELETE','GET'])
def deletedata(request,id):
    try:
        Student=student.objects.get(id=id)

    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    student.delete()

    return Response(
        {
            "message":"Data Deleted Successfully"
        }
    )

#INDEX PAGE 
def index(request):
    url="http://127.0.0.1:8000/getdata/"
    req=requests.get(url)
    data=req.json()
    print(data)
    return render(request,'index.html',{'data':data})

# username : richa19
# password: richa@123 
