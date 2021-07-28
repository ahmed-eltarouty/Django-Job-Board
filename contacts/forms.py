from django import forms
from .models import ContactUs


class ContactUs_Form(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        fields = '__all__'