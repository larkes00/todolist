from django.contrib.auth.models import User
from django.db import models
from treebeard.mp_tree import MP_Node


class List(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название списка")
    image = models.ImageField(upload_to="images/%Y/%m/%d/", verbose_name="Фото")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Задача")
    description = models.TextField(blank=True, verbose_name="Описание")
    completed = models.BooleanField(default=False, verbose_name="Задача завершена")
    list = models.ForeignKey(List, on_delete=models.CASCADE, verbose_name="Список задач")

    node_order_by = ['title']

    def __str__(self):
        return self.title
