from django import forms
from django.forms import ModelForm
from .models import Service 

class DateInput(forms.DateInput):
    input_type = 'date'

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }