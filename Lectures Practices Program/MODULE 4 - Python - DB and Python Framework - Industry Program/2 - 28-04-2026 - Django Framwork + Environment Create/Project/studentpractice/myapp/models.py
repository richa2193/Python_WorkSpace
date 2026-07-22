from django.db import models

# Create your models here.
class studform(models.Model):
    name=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    dob=models.DateField()
    mobile=models.BigIntegerField()
    city=models.CharField(max_length=25)