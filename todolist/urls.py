from django.urls import path
from .views import *

urlpatterns = [
    path("main/", task_list, name="home"),
    path("task/", new_task, name="task_create"),
    path("list/", new_list, name="list_create")
]