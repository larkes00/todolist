from django.contrib.auth.models import User
from django.db import models
from treebeard.mp_tree import MP_Node


class List(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(MP_Node):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    node_order_by = ['title']

    def __str__(self):
        return self.title
