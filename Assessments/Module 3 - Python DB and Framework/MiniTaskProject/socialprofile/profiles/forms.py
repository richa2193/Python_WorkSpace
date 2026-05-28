from django import forms
from .models import profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = profile
        fields = '__all__'

    def clean_age(self):
        age = self.cleaned_data.get('age')

        if age < 13:
            raise forms.ValidationError("User must be above 13 years old.")

        return age