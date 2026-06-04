from rest_framework import serializers
from .models import Doctor, Appointment
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_contact(self, value):

        if not value.isdigit():
            raise serializers.ValidationError(
                "Contact number must contain digits only."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Contact number must be exactly 10 digits."
            )

        return value

    def validate_email(self, value):

        if Doctor.objects.filter(email=value).exists():

            if self.instance and self.instance.email == value:
                return value

            raise serializers.ValidationError(
                "Doctor with this email already exists."
            )

        return value


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password'
        ]

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        UserProfile.objects.create(
            user=user
        )

        return user


class AppointmentSerializer(serializers.ModelSerializer):

    doctor = DoctorSerializer(read_only=True)

    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(),
        source='doctor',
        write_only=True
    )

    class Meta:
        model = Appointment
        fields = [
            'id',
            'doctor',
            'doctor_id',
            'patient_name',
            'patient_email',
            'appointment_date',
            'appointment_time',
            'status',
            'created_at'
        ]

    def validate_patient_email(self, value):

        if "@" not in value:
            raise serializers.ValidationError(
                "Invalid email address."
            )

        return value