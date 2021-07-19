from django.forms import ModelForm
from django import forms
from .models import RegisteredUser

class RegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegisteredUser
        fields = '__all__'
        labels = {
            "name": "Username",
            "email": "Email address",
            "phoneNum": "Phone Number",
            "password": "Password"
        }