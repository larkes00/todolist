from django.urls import path
from .views import *

urlpatterns = [
    path("tasks/", TaskList.as_view(), name="home"),
    path("lists/<int:pk>/", ShowList.as_view(), name="get_list"),
    path("task/", NewTask.as_view(), name="task_create"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", user_logout, name="logout")
]
