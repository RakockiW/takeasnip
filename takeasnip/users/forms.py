from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'bg-zinc-900 text-white px-4 py-2 rounded focus:outline-none focus:ring-2 focus:ring-green-400 border border-transparent hover:border-white transition'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-zinc-900 text-white px-4 py-2 rounded focus:outline-none focus:ring-2 focus:ring-green-400 border border-transparent hover:border-white transition'
    }))

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
        'class': 'bg-zinc-900 text-white px-4 py-2 rounded focus:outline-none focus:ring-2 focus:ring-green-400 border border-transparent hover:border-white transition'
    }))
    password1 = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={
        'class': 'bg-zinc-900 text-white px-4 py-2 rounded focus:outline-none focus:ring-2 focus:ring-green-400 border border-transparent hover:border-white transition'
    }))

    password2 = forms.CharField(
        label="confirm_password",
        widget=forms.PasswordInput(attrs={
        'class': 'bg-zinc-900 text-white px-4 py-2 rounded focus:outline-none focus:ring-2 focus:ring-green-400 border border-transparent hover:border-white transition'
    }))