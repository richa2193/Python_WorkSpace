from django.db import models

class patient(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    birthdate=models.DateField(null=True, blank=True)
    age=models.IntegerField()
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

class Register(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name




# Create your models here.
