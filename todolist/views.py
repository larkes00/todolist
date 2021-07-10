from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from todolist.forms import AddTaskForm, RegisterUserForm, LoginUserForm
from .models import *


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "todolist/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "todolist/login.html"

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        if next_url:
            return next_url

        return reverse('home')


def user_logout(request):
    logout(request)
    return redirect("login")


class TaskList(ListView):
    model = Task
    template_name = "todolist/index.html"
    context_object_name = "tasks"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = [{"x": 1}, {"x": 2}]
        context["something"] = 'Information'
        return context

    def get_queryset(self):
        return Task.objects.filter(completed=False)


class UserLists(ListView):
    model = List
    template_name = "todolist/index.html"
    context_object_name = "lists"

    def get_queryset(self):
        return List.objects.filter(owner=self.request.user.pk)


class ShowList(DetailView):
    model = List
    template_name = "todolist/task.html"
    context_object_name = "task"

    # def get_queryset(self):
    # return Task.objects.filter(list=self.pk)


class NewTask(CreateView):
    form_class = AddTaskForm
    template_name = "todolist/add_task.html"
    success_url = reverse_lazy("home")
