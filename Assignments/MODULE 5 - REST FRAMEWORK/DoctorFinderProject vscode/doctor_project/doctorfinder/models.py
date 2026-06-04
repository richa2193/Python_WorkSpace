from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):

    name = models.CharField(max_length=100)

    specialty = models.CharField(max_length=100)

    city = models.CharField(max_length=100)

    contact = models.CharField(max_length=15)

    email = models.EmailField(unique=True)

    image = models.ImageField(
        upload_to='doctors/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name


class Appointment(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    patient_name = models.CharField(max_length=100)

    patient_email = models.EmailField()

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.doctor.name}"
    
class UserProfile(models.Model):

    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='USER'
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
class Payment(models.Model):

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE
    )

    amount = models.IntegerField()

    razorpay_order_id = models.CharField(
        max_length=200
    )

    razorpay_payment_id = models.CharField(
        max_length=200,
        blank=True
    )

    status = models.CharField(
        max_length=50,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.razorpay_order_id
    

