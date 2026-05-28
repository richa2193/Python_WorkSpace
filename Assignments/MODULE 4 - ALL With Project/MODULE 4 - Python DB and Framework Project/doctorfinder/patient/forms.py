from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class patientform(forms.ModelForm):
    class Meta:
        model=patient
        fields='__all__'

class RegisterForm(forms.ModelForm):

    class Meta:
        model=Register
        fields = '__all__'

class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:

        model = User

        fields = ['username', 'email', 'password1', 'password2']


class UpdateProfileForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ['username', 'email']