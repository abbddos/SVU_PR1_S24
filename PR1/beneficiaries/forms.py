from django import forms
from django.forms import ModelForm
from .models import Beneficiary

class DateInput(forms.DateInput):
    input_type = 'date'

class BeneficiaryForm(ModelForm):
    class Meta:
        model = Beneficiary
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(),
            'last_updated_by': forms.HiddenInput()
        }