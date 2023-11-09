from django import forms
from .models import customer

class customerForm (forms.ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
        

