from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import *


class CreateTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["list"].empty_label = "Список не выбран"

    class Meta:
        model = Task
        fields = ["title", "description", "list"]
        widgets = {
            "description": forms.Textarea(attrs={"cols": 40, "rows": 10})
        }


class CreateListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["name"]


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=(forms.PasswordInput(attrs={"class": "register-form"})))
    password2 = forms.CharField(
        label="Confirm Password",
        widget=(forms.PasswordInput(attrs={"class": "register-form"}))
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "register-form"}),
            "email": forms.EmailInput(attrs={"class": "register-form"}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "login-form"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "login-form"}))
