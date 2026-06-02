from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task

class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('todo:task-list')

class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('todo:task-list')

class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('todo:task-list')
    template_name = "todo/task_delete.html"

def toggle_status(request:HttpRequest, pk) -> HttpResponse:
    if request.method == "POST":
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        task.save()
    return redirect("todo:task-list")



class TagListView(generic.ListView):
    model = Tag

class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")

class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")

class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_delete.html"
