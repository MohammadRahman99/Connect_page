from .models import *
from django import forms



class ContactForm(forms.ModelForm):
     class Meta:
        model = ContactInfo
        fields = '__all__'