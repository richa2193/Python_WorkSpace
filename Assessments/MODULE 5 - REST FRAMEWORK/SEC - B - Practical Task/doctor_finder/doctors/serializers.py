from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty")
        return value