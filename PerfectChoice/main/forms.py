from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


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


class UserUpdateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username-field'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-field'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-confirm-field'}))
    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)