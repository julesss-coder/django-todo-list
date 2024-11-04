from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskModel

# Create your views here.
# tasks/views.py

def home(request):
    tasks = TaskModel.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/home.html', context)