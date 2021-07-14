from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from todolist.forms import RegisterUserForm, LoginUserForm, CreateListForm
from .models import *
from .utils import DataMixin


class TaskList(LoginRequiredMixin, DataMixin, ListView):
    model = Task
    template_name = "todolist/index.html"
    context_object_name = "tasks"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(user=self.request.user.id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Task.objects.filter(completed=False)


class ShowTask(LoginRequiredMixin, DataMixin, DetailView):
    model = Task
    template_name = "todolist/task_info.html"
    context_object_name = "task"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.filter(list=context["task"].list.pk)
        c_def = self.get_user_context(user=self.request.user.id)
        return dict(list(context.items()) + list(c_def.items()))


class UserLists(LoginRequiredMixin, DataMixin, ListView):
    template_name = "todolist/index.html"
    context_object_name = "lists"

    def get_queryset(self):
        return List.objects.filter(owner=self.request.user.pk)


class ListTasks(LoginRequiredMixin, DataMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todolist/list_tasks.html"

    def get_queryset(self):
        return Task.objects.filter(list=self.kwargs["pk"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(user=self.request.user.id)
        return dict(list(context.items()) + list(c_def.items()))


class NewUserList(LoginRequiredMixin, CreateView):
    form_class = CreateListForm
    template_name = "todolist/new_list.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


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
