from django import forms

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(attrs={"class": "datepicker", "type": "datetime-local"})
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(),
    )
    class Meta:
        model = Task
        fields = "__all__"



class TagForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
