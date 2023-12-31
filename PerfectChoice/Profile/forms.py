from django import forms

from .models import *


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'profile_image', 'birth_date', 'interests']
        widgets = {'birth_date': forms.DateInput(attrs={'type': 'date'})}
