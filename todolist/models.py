from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from treebeard.mp_tree import MP_Node


class List(models.Model):
    name = models.CharField(max_length=128, verbose_name="List name")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list', kwargs={"pk": self.pk})


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Task")
    description = models.TextField(blank=True, verbose_name="Description")
    completed = models.BooleanField(default=False, verbose_name="Task status")
    list = models.ForeignKey(List, on_delete=models.CASCADE, verbose_name="Task list")

    node_order_by = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_info', kwargs={"pk": self.pk})


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)
