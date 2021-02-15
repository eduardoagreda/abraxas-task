from django.contrib import admin

# Register your models here.

from apps.task.models import Task

admin.site.register(Task)