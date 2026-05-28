from django.db import models


class doctor(models.Model):

    name = models.CharField(max_length=100)

    specialization = models.CharField(max_length=100)

    experience = models.IntegerField()

    city = models.CharField(max_length=100)

    email = models.EmailField(blank=True, null=True)

    phone = models.CharField(max_length=15, blank=True, null=True)

    hospital = models.CharField(max_length=100, blank=True, null=True)

    available_time = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):

        return self.name