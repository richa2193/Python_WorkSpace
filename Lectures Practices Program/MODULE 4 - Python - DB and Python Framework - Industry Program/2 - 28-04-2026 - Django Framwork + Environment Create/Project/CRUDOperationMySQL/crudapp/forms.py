from django import forms
from .models import studinfo

class studform(forms.ModelForm):
    class Meta:
        model = studinfo
        fields='__all__'

        