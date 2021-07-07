from django.urls import path
from .views import *

urlpatterns = [
    path("main/", start, name="main"),
    path("task/", new_task, name="task_create")
]