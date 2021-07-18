from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from todolist.forms import RegisterUserForm, LoginUserForm, CreateListForm, CreateTaskForm
from .models import *
from .utils import DataMixin


class ShowTask(LoginRequiredMixin, DataMixin, DetailView):
    model = Task
    template_name = "todolist/task_info.html"
    context_object_name = "task"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.filter(list=context["task"].list.pk)
        c_def = self.get_user_context(user=self.request.user.id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_object(self, queryset=None):
        obj = super(ShowTask, self).get_object(queryset)
        if not obj.list.owner.id == self.request.user.pk:
            raise PermissionDenied

        return obj


class UserLists(LoginRequiredMixin, DataMixin, ListView):
    template_name = "todolist/index.html"
    context_object_name = "lists"

    def get_queryset(self):
        return List.objects.filter(owner=self.request.user.pk)


class Tasks(LoginRequiredMixin, DataMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todolist/tasks_list.html"

    def get_queryset(self):
        return Task.objects.filter(list=self.kwargs["pk"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(user=self.request.user.id)
        return dict(list(context.items()) + list(c_def.items()))


class ShowList(LoginRequiredMixin, DetailView):
    model = List
    context_object_name = "list"
    template_name = "todolist/list_info.html"

    def get_object(self, queryset=None):
        obj = super(ShowList, self).get_object(queryset)
        if not obj.owner.id == self.request.user.pk:
            raise PermissionDenied

        return obj


class NewUserList(LoginRequiredMixin, CreateView):
    form_class = CreateListForm
    template_name = "todolist/list_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CreateTask(LoginRequiredMixin, CreateView):
    form_class = CreateTaskForm
    template_name = "todolist/task_form.html"
    success_url = reverse_lazy("home")


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("home")


class DeleteList(LoginRequiredMixin, DeleteView):
    model = List
    context_object_name = "list"
    success_url = reverse_lazy("home")


class UpdateList(LoginRequiredMixin, UpdateView):
    model = List
    form_class = CreateListForm
    success_url = reverse_lazy("home")


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = CreateTaskForm
    success_url = reverse_lazy("home")


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
    redirect_authenticated_user = "next"

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        if next_url:
            return next_url

        return reverse('home')


def user_logout(request):
    logout(request)
    return redirect("login")
