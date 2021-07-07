from django import forms
from .models import *


class AddTaskForm(forms.Form):
    title = forms.CharField(max_length=255)
    list = forms.ModelChoiceField(queryset=List.objects.all())


class AddListForm(forms.Form):
    name = forms.CharField(max_length=128)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
