from django import forms

from django.forms import TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username'
        }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
        }),
            'password1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'password1'
        }),
            'password2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'password2'
        }),
        }

class LoginUserForm(AuthenticationForm):
    email = forms.CharField(widget= forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control'}))