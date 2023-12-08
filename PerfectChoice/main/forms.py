from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *


class UserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'email'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'User name', 'class': 'input'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'password'}),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password', 'class': 'password'}),
        label="Repeat password"
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
