from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from . models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'username',
        'placeholder': 'Name'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password',
        'placeholder': 'Password'

    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'username  ',
        'placeholder': 'Username'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'email',
        'placeholder': 'Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password1',
        'placeholder': 'Password'

    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password2',
        'placeholder': 'Repeat password'

    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'readonly': True,
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'readonly': True,
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
    }), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'image']
