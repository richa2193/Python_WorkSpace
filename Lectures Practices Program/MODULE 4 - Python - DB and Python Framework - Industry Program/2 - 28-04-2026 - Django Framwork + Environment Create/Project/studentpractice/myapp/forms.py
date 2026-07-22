from django import forms
from .models import *

class studinfo(forms.ModelForm):
    class Meta:
        model=studform
        fields='__all__'