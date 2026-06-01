from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task


class TaskListView(generic.ListView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["next"] =self.request.META.get("HTTP_REFERER")
        return context

class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('task_list')

class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('todo:task-list')

class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = "todo/task_delete.html"



