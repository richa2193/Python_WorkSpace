from django.db import models

# Create your models here.
class userprofile(models.Model):
    username=models.CharField(max_length=50)
    age=models.IntegerField()
    is_public=models.BooleanField(default=True)

    def __str__(self):
        return self.username