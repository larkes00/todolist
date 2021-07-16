from django.urls import path
from .views import *

urlpatterns = [
    path("", UserLists.as_view(), name="home"),
    path("list/<int:pk>/tasks/", Tasks.as_view(), name="list"),
    path("list/create/", NewUserList.as_view(), name="create_list"),
    path("list/<int:pk>/", ShowList.as_view(), name="list_info"),
    path("task/<int:pk>/", ShowTask.as_view(), name="task_info"),
    path("task/create/", CreateTask.as_view(), name="task_form"),
    path("task/delete/<int:pk>/", DeleteTask.as_view(), name="task_delete"),
    path("list/delete/<int:pk>/", DeleteList.as_view(), name="list_delete"),
    path("list/update/<int:pk>/", UpdateList.as_view(), name="update_list"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", user_logout, name="logout")
]
