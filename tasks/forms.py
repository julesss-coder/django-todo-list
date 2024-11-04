from .models import TaskModel
from django import forms

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add in a new task'}))

    class Meta:
        model = TaskModel
        fields = "__all__"

