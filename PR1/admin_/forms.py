from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile

class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']