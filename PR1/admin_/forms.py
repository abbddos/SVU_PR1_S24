from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile

class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'is_active']

class UserProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['role']