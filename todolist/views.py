from django.shortcuts import render

from todolist.forms import AddTaskForm


def start(request):
    return render(request, "todolist/index.html", {"foo": "bar"})


def new_task(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddTaskForm()

    return render(request, "todolist/add_task.html", {"form": form})
