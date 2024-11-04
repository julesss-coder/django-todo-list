from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskModel
from .forms import TaskForm

# Create your views here.
# tasks/views.py

def home(request):
    form = TaskForm()
    tasks = TaskModel.objects.all()
    context = {'tasks': tasks, 'TaskForm': form}
    return render(request, 'tasks/home.html', context)