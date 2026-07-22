from rest_framework import serializers
from .models import *

class studserial(serializers.ModelSerializer):
    class Meta:
        model = studinfo
        fields = '__all__'
        