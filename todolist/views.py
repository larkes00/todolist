from django.shortcuts import render, redirect

from todolist.forms import AddTaskForm, AddListForm
from .models import *


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "todolist/index.html", {"tasks": tasks})


def new_task(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddTaskForm()

    return render(request, "todolist/add_task.html", {"form": form})


def new_list(request):
    if request.method == "POST":
        form = AddListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddListForm()

    return render(request, "todolist/add_list.html", {"form": form})
