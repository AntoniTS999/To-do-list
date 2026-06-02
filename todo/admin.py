from django.contrib import admin
from django.contrib.auth.models import Group

from todo.models import Task, Tag


admin.site.register(Tag)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content","datetime", "deadline", "completed")
    list_filter = ("deadline", "completed")
    search_fields = ["content"]

admin.site.unregister(Group)
