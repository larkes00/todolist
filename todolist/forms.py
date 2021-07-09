from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import *


class AddTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["list"].empty_label = "Список не выбран"

    class Meta:
        model = Task
        fields = ["title", "description", "list"]
        widgets = {
            "description": forms.Textarea(attrs={"cols": 40, "rows": 10})
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) > 255:
            raise ValidationError("Длина превышает 255 символов")

        return title


class AddListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["name", "image"]


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
