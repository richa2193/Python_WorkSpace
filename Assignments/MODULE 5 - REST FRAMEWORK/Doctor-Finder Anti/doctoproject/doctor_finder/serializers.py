from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    """Serializer for the Doctor model, exposing all fields.

    The serializer includes validation inherited from the model validators.
    """

    class Meta:
        model = Doctor
        fields = [
            "id",
            "name",
            "specialty",
            "contact",
            "email",
            "experience_years",
            "clinic_address",
            "available_days",
            "consultation_fee",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
