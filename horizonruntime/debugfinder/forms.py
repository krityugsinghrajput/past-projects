from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Please enter your username", max_length=255, required=True)
    password = forms.CharField(label="Please enter your password", max_length=155 required=True)