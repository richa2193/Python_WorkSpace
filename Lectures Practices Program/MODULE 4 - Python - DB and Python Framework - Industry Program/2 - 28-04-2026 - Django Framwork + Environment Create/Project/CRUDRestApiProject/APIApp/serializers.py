from rest_framework import serializers
from .models import *

class studserial(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'