from django import forms
from django.contrib.auth.models import User
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['added_by',]


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            "password": forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
