from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import EmployeeSignUp
from django import forms


class EmployeeSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class EmployeeLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")


class UpdateEmployeeForm(forms.ModelForm):
    information = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = EmployeeSignUp
        exclude = ["user"]
