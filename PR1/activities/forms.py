from django import forms
from django.forms import DateInput
from django.forms import ModelForm
from .models import Activity


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        widgets = {
            'service': forms.TextInput(),
            'beneficiary': forms.TextInput(),
            'last_updated_by': forms.HiddenInput()
        }




class EventForm(forms.Form):
    start_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    report_type = forms.ChoiceField(choices=[('4Ws', '4Ws'), ('Infographic', 'Infographic')]) 