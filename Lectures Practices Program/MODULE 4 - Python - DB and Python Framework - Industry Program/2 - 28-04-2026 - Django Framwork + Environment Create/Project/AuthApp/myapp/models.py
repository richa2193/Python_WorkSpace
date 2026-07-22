from django.db import models

# Create your models here.
class Usersignup(models.Model):
    fullname=models.CharField(max_length=25)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=12)