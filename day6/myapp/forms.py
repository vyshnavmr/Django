from django import forms
from django.core.validators import validate_email
from django.core.validators import ValidationError


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=6)