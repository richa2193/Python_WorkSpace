from django.db import models

# Create your models here.
class profile(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
    bio=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
    
    