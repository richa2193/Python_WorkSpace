from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone

class Doctor(models.Model):
    """Model representing a medical doctor.

    Fields include basic contact info, specialty, experience, and
    availability. Validation is applied at the model level.
    """

    name = models.CharField(max_length=150, help_text="Full name of the doctor")
    specialty = models.CharField(max_length=100, help_text="Medical specialty/department")
    # Simple phone number validation (allows digits, +, -, spaces)
    phone_regex = RegexValidator(regex=r"^[+\d][\d\s\-]{6,20}$",
                                 message="Enter a valid contact number.")
    contact = models.CharField(validators=[phone_regex], max_length=20,
                               help_text="Contact phone number")
    email = models.EmailField(unique=True, help_text="Professional email address")
    experience_years = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        help_text="Number of years of experience"
    )
    clinic_address = models.TextField(help_text="Full address of the clinic/hospital")
    # Store days as a comma‑separated string (e.g., "Mon,Tue,Wed")
    available_days = models.CharField(
        max_length=100,
        help_text="Comma‑separated list of days the doctor is available"
    )
    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Fee charged per consultation"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.specialty})"


class Appointment(models.Model):
    """Model representing a patient appointment with a doctor.

    * `patient_name`, `patient_email`, `patient_phone` – basic contact info.
    * `doctor` – FK to the `Doctor` model.
    * `appointment_date` and `appointment_time` – stored separately for
      flexibility but validated together to ensure the datetime is in the future.
    * `payment_status` – simple choice field (Paid / Pending / Failed).
    * `booking_status` – indicates if the slot is confirmed or cancelled.
    * `created_at` – timestamp of booking creation.
    """

    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    ]

    BOOKING_STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('pending', 'Pending'),
    ]

    patient_name = models.CharField(max_length=150, help_text="Patient's full name")
    patient_email = models.EmailField(help_text="Patient's email address")
    patient_phone = models.CharField(max_length=20, help_text="Patient's contact number")
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField(help_text="Date of the appointment")
    appointment_time = models.TimeField(help_text="Time of the appointment")
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    booking_status = models.CharField(max_length=10, choices=BOOKING_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-appointment_date', '-appointment_time']
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return f"{self.patient_name} - {self.doctor.name} on {self.appointment_date}"

    def clean(self):
        """Validate that the appointment is scheduled for a future datetime.

        Combines `appointment_date` and `appointment_time` and compares with
        the current timezone‑aware datetime.
        """
        from django.core.exceptions import ValidationError
        import datetime
        appointment_dt = datetime.datetime.combine(self.appointment_date, self.appointment_time)
        # Make timezone‑aware if settings.USE_TZ is True
        if timezone.is_aware(appointment_dt):
            now = timezone.now()
        else:
            now = timezone.now().replace(tzinfo=None)
        if appointment_dt <= now:
            raise ValidationError('Appointment must be set for a future date and time.')

        pass
