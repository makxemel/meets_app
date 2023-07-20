from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import User


class RegisterClientForm(UserCreationForm):
    genders = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    gender = forms.ChoiceField(choices=genders)

    class Meta:
        model = User
        fields = ('avatar', 'first_name', 'last_name', 'gender', 'email', 'password1', 'password2')
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control-file'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-check-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class LoginUserForm(AuthenticationForm):
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # password = forms.CharField(
    #     label='Password',
    #     widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    # )
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }