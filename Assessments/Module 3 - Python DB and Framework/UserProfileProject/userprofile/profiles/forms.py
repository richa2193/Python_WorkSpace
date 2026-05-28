from django import forms
from .models import userprofile

class userprofileform(forms.ModelForm):
    class Meta:
        model=userprofile
        fields="__all__"

    def clean_age(self):
        age=self.cleaned_data.get('age')

        if age < 13:
            raise forms.ValidationError("User Must be above 13 years old.")
        
        return age 