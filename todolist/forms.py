from django import forms
from .models import *


class AddTaskForm(forms.Form):
    title = forms.CharField(max_length=255, label="Задача")
    description = forms.CharField(
        widget=forms.Textarea(attrs={"cols": 30, "rows": 10}),
        label="Описание задачи",
        required=False
    )
    list = forms.ModelChoiceField(queryset=List.objects.all(), label="Список", empty_label="Список не выбран")


class AddListForm(forms.Form):
    name = forms.CharField(max_length=128, label="Название списка")
