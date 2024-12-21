from django import forms
from django.forms import ModelForm
from .models import Activity


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        widgets = {
            'service': forms.TextInput(),
            'beneficiary': forms.TextInput(),
        }
