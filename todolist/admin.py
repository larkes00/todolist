from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import *


# Register your models here.

class TaskAdmin(TreeAdmin):
    form = movenodeform_factory(Task)


admin.site.register(List)
admin.site.register(Task, TaskAdmin)
