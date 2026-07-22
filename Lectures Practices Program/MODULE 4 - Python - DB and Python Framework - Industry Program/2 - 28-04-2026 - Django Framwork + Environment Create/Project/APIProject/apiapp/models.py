from django.db import models

# Create your models here.
class studinfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    dob = models.DateField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name