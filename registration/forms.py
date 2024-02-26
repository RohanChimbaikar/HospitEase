from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        db_table = 'registration_registration'
        fields = ['first_name','last_name','username','password','phone_number','gender']

