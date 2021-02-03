from django import forms
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        min_length=4,
        max_length=50,
        label='Ваше имя',
    )

    last_name = forms.CharField(
        min_length=4,
        max_length=50,
        label='Ваша фамилия'
    )

    email = forms.EmailField(
        max_length=50,
        min_length=10,
        widget=forms.EmailInput(),
        label='Email'
    )

