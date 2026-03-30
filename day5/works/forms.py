from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=50)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, max_length=20)