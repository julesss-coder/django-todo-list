from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TaskModel
from .forms import TaskForm

# Create your views here.
# tasks/views.py

def home(request):
    tasks = TaskModel.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'TaskForm': form}
    return render(request, 'tasks/home.html', context)

