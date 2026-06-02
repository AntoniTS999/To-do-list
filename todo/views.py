from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["next"] =self.request.META.get("HTTP_REFERER")
        return context

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

