from django.shortcuts import render, redirect

from todolist.forms import AddTaskForm
from .models import *


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "todolist/index.html", {"tasks": tasks})


def new_task(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            try:
                Task.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, "Ошибка добавления задачи")
    else:
        form = AddTaskForm()

    return render(request, "todolist/add_task.html", {"form": form})
