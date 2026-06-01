from django.urls import path
from todo.views import (TaskListView,
                        TaskCreateView,
                        TaskUpdateView)

app_name="todo"
urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create"),path("tasks/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
]