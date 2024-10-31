from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# tasks/views.py

def home(request):
    return render(request, 'tasks/home.html')