from django.contrib.auth.forms import AuthenticationForm
from django import forms
from . models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'your_name',
        'placeholder': 'Your Name'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'your_pass',
        'placeholder': 'Password'

    }))

    class Meta:
        model = User
        fields = ['username', 'password']
